# %%
import pandas as pd
# %%
from dash import Dash, html, dcc, Input, Output, State
# %%
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
# %%
path = '~/timeseer/data/dummy.csv'

df = pd.read_csv(path)

available_dims = [attr for attr in df.columns.tolist() \
    if df[attr].dtype.name == 'object']

available_metrs = [metr for metr in df.columns.tolist() \
    if df[metr].dtype.name != 'object'][1:]

