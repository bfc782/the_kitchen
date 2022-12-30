# %%
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go

path = '~/timeseer/data/trades.csv'

df = pd.read_csv(path)

# %%
app = Dash(
    __name__, 
    title='Callback on Trades.csv',
    external_stylesheets=[dbc.themes.COSMO]
)

if __name__ == '__main__':
    app.run_server(debug=True)