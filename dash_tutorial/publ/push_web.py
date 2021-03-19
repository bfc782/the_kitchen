import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
#import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('outp_sim.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Div(id='my-output'),
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app.layout = html.Div(children=[
    html.H4(children='Sim_pipeline_in_progress!'),
    generate_table(df),
    dcc.Interval(
        id='interval-component',
        interval=1*10000,
        n_intervals=0
    )
])

@app.callback(
    Output('my-output','children'),
    Input('interval-component', 'n_intervals')
)
def update(n):
    df = pd.read_csv('outp_sim.csv')
    return df
    
if __name__ == '__main__':
    app.run_server(debug=True)
