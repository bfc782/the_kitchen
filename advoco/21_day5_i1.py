# %%

coord_rows = []
with open('21_day5_i.txt', 'r') as f:
    for line in f:
        # coord_rows.append(line.split(' ->'))
        coord_rows.append(line.split())
        
# %%
coords_clean = []
for i in coord_rows:
    for j in i:
        coords_clean.append([int(x) for x in j.split(',')])

# %%
coord_count = len(coords_clean)
coord_group_list = [[i, i+1] for i in range(0,coord_count,2)]

coords_grouped = []
for i in coord_group_list:
    coords_grouped.append([coords_clean[i[0]], coords_clean[i[1]]])
# %%
import numpy as np

# my_arr = np.zeros(shape=(10,10))
my_arr = np.zeros(shape=(990,990))

# %%
match = []
for i in coords_grouped:
    if (i[0][0] == i[1][0]) | (i[0][1] == i[1][1]):
        match.append(i)
# %%
paired = [] 
for i in match:
    if i[0][0]==i[1][0]:
        paired.append([[i[0][0]],[i[1][0], i[1][1]]])
    else:
        paired.append([[i[0][0], i[1][0]], [i[1][1]]])

# %%
for i in paired:
    for j in i: 
        j.sort()

# %%
y, x = 0, 0
for i in paired:
    [y, x] = i
    if len(x) == 1:
        my_arr[x[0], y[0]:y[1]+1] += 1
        # print(my_arr[x[0], y[0]:y[1]])
    else:
        my_arr[x[0]:x[1]+1, y[0]] += 1
        # print(my_arr[x[0]:x[1], y[0]])

# %%
my_arr
# %%
