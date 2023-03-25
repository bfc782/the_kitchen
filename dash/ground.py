# %%
import pandas as pd
import os
# %%
from dash import Dash, html, dcc, Input, Output

# %%
PATH = '~/model/'
FILE = 'mockup.xlsx'
df = pd.read_excel(PATH + FILE, sheet_name='forge', skiprows=1)


# %%
