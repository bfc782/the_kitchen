#%% f.readline(), f.readlines(), 
#%%
import pandas as pd
import re

df = pd.read_csv('day04_input.csv')
# %%
mylist =[]
with open('day04_input.csv') as f:
    # count_lines = len(f.readlines())

    for i in range(986):
        mylist.append(re.sub('[\\n]','',f.readline()))
print(mylist)
# %%
