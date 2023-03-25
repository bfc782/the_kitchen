# %%
import pandas as pd
# %%
from dash import Dash, html, dcc, Input, Output, State
# %%
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
# %%
path = '~/timeseer/data/trades.csv'

df = pd.read_csv(path).head(1000)

ccys = df['tx_ccy'].unique()

available_dims = [attr for attr in df.columns.tolist() \
    if df[attr].dtype.name == 'object']

init_dim_options = list(df[available_dims[-1]].value_counts().index)
# init_dim_options = [{'label': i, 'value': i} for i in init_dim_options]

available_metrs = [metr for metr in df.columns.tolist() \
    if df[metr].dtype.name != 'object'][1:]

available_metrs = ['tx_nom']

init_metr_options = list(df[available_metrs[-1]].value_counts().index)


# %%
app = Dash(
    __name__, 
    title='Callback on Trades.csv',
    external_stylesheets=[dbc.themes.COSMO]
)

@app.callback(
    Output('chosen-metr-radio', 'value'),
    Input('chosen-metr-radio', 'value')
)
def update_metr(chosen_metr):
    metr_value = chosen_metr
    return metr_value    

@app.callback(
    Output('chosen-dim-dropdown', 'options'),
    Output('chosen-dim-dropdown', 'value'),
    Input('chosen-dim-radio', 'value')
)
def update_dropdown(chosen_dim):
    # dff_dim_options = df[chosen_dim].unique()  
    dd_options = list(df[chosen_dim].value_counts().index)
    dd_value = dd_options[0]
    dd_options = [{'label': i, 'value': i} for i in dd_options]
    return dd_options, dd_value    

@app.callback(
    Output('indicator-graphic', 'figure'),
    # Input('chose-dim-radio', 'value'),
    Input('chosen-dim-dropdown', 'value'),
    State('chosen-dim-radio', 'value'),
    State('chosen-metr-radio', 'value')
    )
def update_graph(attribute_filter, chosen_attribute, chosen_metr):#, yaxis_column_name):
    # print(attribute_filter, chosen_attribute)
    dff = df[df[chosen_attribute] == attribute_filter]

    dff = dff.groupby(['date', chosen_metr]).sum()\
                .reset_index()

    fig = px.bar(x=dff['date'], 
                    y=dff[chosen_metr])
                    #  y=dff[dff['tx_ccy'] == yaxis_column_name]['Value'],
                    #  hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])
    return fig

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.RadioItems(
                id='chosen-dim-radio',
                options=[{'label': i, 'value': i} for i in available_dims],
                value=available_dims[-1]
            )

        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
        
        html.Div([
            dcc.RadioItems(
                id='chosen-metr-radio',
                options=[{'label': i, 'value': i} for i in available_metrs],
                value=available_metrs[-1]
            )

        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='chosen-dim-dropdown',
                options=[{'label': i, 'value': i} for i in init_dim_options],
                value=init_dim_options[0]
            )

        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    dcc.Graph(id='indicator-graphic'),
])

if __name__ == '__main__':
    app.run_server(debug=True)