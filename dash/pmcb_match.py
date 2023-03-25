# %%
from dash import Dash, dcc, html, Input, Output, State, MATCH, ALL
import pandas as pd

trade_file = '~/timeseer/data/trades.csv'
df = pd.read_csv(trade_file, sep=',')

df_cols = df.columns.tolist()

# %%
app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Button("Add Filter", id="dynamic-add-filter", n_clicks=0),
    html.Div(id='dynamic-dropdown-container', children=[]),
])

@app.callback(
    Output('dynamic-dropdown-container', 'children'),
    # Input('dynamic-dropdown-container', 'children'),
    Input('dynamic-add-filter', 'n_clicks'),
    State('dynamic-dropdown-container', 'children')
    )
def display_dropdowns(
        # df, 
        n_clicks, children):

    if type(df) is not list:
        df_cols = df.columns.tolist()
    else:
        df_cols = df

    new_element = html.Div([
        dcc.Dropdown(
            df_cols, 
            # ['NYC', 'MTL', 'LA', 'TOKYO'],
            id={
                'type': 'dynamic-dropdown',
                'index': n_clicks
            }
        ),
        html.Div(
            id={
                'type': 'dynamic-output',
                'index': n_clicks
            }
        )
    ])
    children.append(new_element)
    # return df_cols, children
    return children


@app.callback(
    Output({'type': 'dynamic-output', 'index': MATCH}, 'children'),
    Input({'type': 'dynamic-dropdown', 'index': MATCH}, 'value'),
    State({'type': 'dynamic-dropdown', 'index': MATCH}, 'id'),
)
def display_output(value, id):
    return html.Div('Dropdown {} = {}'.format(id['index'], value))


if __name__ == '__main__':
    app.run_server(debug=True)
