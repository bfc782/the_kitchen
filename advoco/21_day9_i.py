# %%

import numpy as np
import pandas as pd
import re

grid_list = []
# with open('21_day9_test.txt', 'r') as f:
with open('21_day9_i.txt', 'r') as f:
    for line in f:
        line = re.sub('[\D]','',line)
        grid_list.append([int(j) for i, j in enumerate(line)])
    
# print(grid_list)
# %%

arr = np.array(grid_list)

slices_lr = [slice(max(0, i - 1), min(arr.shape[1]+1, i + 2)) \
                for i, _ in enumerate(arr[0])]

slices_ud = [slice(max(0, i - 1), min(arr.shape[0]+1, i + 2)) \
                for i, _ in enumerate(arr.T[0])]

local_min = np.array([[arr[i, j].min() + 1 if arr[row, col] == arr[i, j].min() else 0 \
                                        for col, j in enumerate(slices_lr)] \
                                            for row, i in enumerate(slices_ud)])

print(local_min.sum())
# %% depth first search algo





# %% ignore this... test of 3-d perspective!
arr_3d = np.zeros(shape=(arr.shape[0], arr.shape[1], arr.max() + 1))

for i, row in enumerate(arr[:]):
    for j, elem in enumerate(row):
        arr_3d[i, j, elem] = 1

# %%
'''
each point in a basin will be bound by a 9, or an edge

start from top left:
- move from left to right, up to down to find first basin point
    - is point part of basin? i.e. not 9?

'''
bounds = []
bounded = []
for ix, row in enumerate(arr[:5, :5]):
    bounds.append(np.where(row == 9))
    bounded.append(np.where(row != 9))


# %%
from itertools import product
# %%
def get_children(loc, arr) -> list:
    
    adjnt = []
    row, col = loc

    if row - 1 > 0:
        if arr[row - 1, col] != 9:
            adjnt.append((row - 1, col))
    
    if row + 1 < arr.shape[0]:
        if arr[row + 1, col] != 9:
            adjnt.append((row + 1, col))
    
    if col - 1 > 0:
        if arr[row, col - 1] != 9:
            adjnt.append((row, col - 1))
    
    if col + 1 < arr.shape[0]:
        if arr[row, col + 1] != 9:
            adjnt.append((row, col + 1))

    return adjnt 

# %%
basins = []
for row_ix, row in enumerate(arr[:5, :5]):
    for col_ix, col in enumerate(row):
        if arr[row_ix, col_ix] == 9:
            pass
        else:
            children = get_children((row_ix, col_ix), arr[:5, :5])
            if not basins:
                basins.append(children)
            if children in basins:
                basins.append(children)

        
# %%
