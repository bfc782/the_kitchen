# %%
import pandas as pd
import re
import numpy as np
# %%
# with open('22_day05_test.txt', 'r') as f:
with open('22_day05.txt', 'r') as f:
    out = []
    for line in f:
        print(line)
        if line == '\n':
            break
        line = re.findall('(\S{3}|\s{4})', line)
        line = ['-' if i == '    ' else i[1] for i in line]
        out.append(line)
out = out[:-1]

# %%
rows = len(out)
cols = max(len(row) for row in out)

out_arr = np.zeros(shape=(rows, cols), dtype=object)

# %%
for ix, row in enumerate(out):
    for jx, elem in enumerate(row):
        out_arr[ix, jx] = elem

# %%
np.concate
grid = out
# %%
grid
# %%
grid_np = np.array(grid
# , dtype=object
)
# %%
grid_np.T
# %%
def find_top_of_pile(arr, pile):
    piles_are_rows = arr.T
    piles = []
    for row in piles_are_rows:
        for elem in row:
            piles.append(np.where(elem != '    '))

    return piles

# %%
find_top_of_pile(grid_np, 1)

# %%
my_arr = np.zeros(shape=(2,2), dtype=object)
