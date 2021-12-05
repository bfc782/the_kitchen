# %%
import pandas as pd

# %%

df = pd.read_table('21_day5_test.txt', sep=" ->", header=None)
df.columns = ['col1', 'col2']

# %%
df['col1'][0]

# %%
func_x1 = lambda x: [int(y) for y in x.split(',')]

# %%
df['coord1'] = df['col1'].apply(func_x1)
#%%
df['coord2'] = df['col2'].apply(func_x1)
# %%
