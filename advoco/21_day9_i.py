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

