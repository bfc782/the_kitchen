# %%
import numpy as np

# %%
def coorder(line):
    step1 = line.split()
    [c1, _, c2] = step1
    [x1, y1], [x2, y2] = [int(i) for i in c1.split(',')],\
        [int(j) for j in c2.split(',')]

    if x1 == x2:
        y_arg = sorted([y1, y2])
        y_arg_rng = list(range(y_arg[0],y_arg[1] + 1))
        return [y_arg_rng, x1]
    if y1 == y2:
        x_arg = sorted([x1, x2])
        x_arg_rng = list(range(x_arg[0], x_arg[1] + 1))
        return (y1, x_arg_rng)
    else:
        x_arg = sorted([x1, x2])
        x_arg_rng = list(range(x_arg[0], x_arg[1] + 1))
        if x2 < x1:
            x_arg_rng.reverse()
        y_arg = sorted([y1, y2])
        y_arg_rng = list(range(y_arg[0], y_arg[1] + 1))
        if y2 < y1:
            y_arg_rng.reverse()
        return (y_arg_rng, x_arg_rng)
    
# %%
arr = np.zeros(shape=(1000,1000))
# arr = np.zeros(shape=(10,10))

with open('21_day5_i.txt', 'r') as f:
    for line in f:
        test = coorder(line)
        if test is not None:
            print(test)
            arr[test] += 1

# %%
arr

# %%
count = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i,j] > 1:
            count += 1
count
# %%
