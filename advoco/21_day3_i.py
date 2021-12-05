# %%
import numpy as np
import re

# %%
with open('21day3_i.txt', 'r') as f:
# with open('21_day3_test.txt', 'r') as f:    
    arr = []
    for line in f:
        new_item = [int(line[i]) for i, _ in enumerate(line[:12])]
        # new_item = [int(line[i]) for i, _ in enumerate(line[:5])]
        arr.append(new_item)       
    np_arr = np.array(arr)

# %%
    rows = np_arr.shape[0]
    cols = np_arr.shape[1]
    threshold = rows/2
    gamma = [int(round(np_arr[:,i].sum()/rows,0)) for i in range(cols)]
    epsilon = [int(not(i)) for i in gamma]
    func = lambda x: re.sub("[^\d+]","",str(x))
    # gammabin = re.sub("[^\d+]","",str(gamma))
    gammabin = func(gamma)
    epsilonbin = func(epsilon)
    gammadec = int(gammabin, 2)
    epsilondec = int(epsilonbin, 2)
    print(gammabin, gammadec, epsilonbin, epsilondec)

# %%
# start with np_arr and evaluate bit filter
# start = np_arr

def bit_filter(arr):
    rows = arr.shape[0]
    if 2*arr[:,0].sum() == rows:
        adj = 1
    else:
        adj = 0
    maj = int(round((arr[:,0].sum()+adj)/rows,0))
    min = int(round((arr.shape[0] - arr[:,0].sum())/rows,0))
    return maj, min

# %%
start = np_arr
maj_collect = []
while start.shape[0]>1:
    print(start.shape)   
    maj_bit, min_bit = bit_filter(start)
    fancy = [i for i, j in enumerate(start[:,0]) if j == maj_bit]
    maj_collect.append(bit_filter(start)[0])
    start = start[fancy][:,1:]
    if start.shape[0] == 1:
        maj_collect.append(list(start)) 

print(maj_collect)

ox_gen = int(func(maj_collect),2)
print(ox_gen)
# %%
start = np_arr
min_collect = []
while start.shape[0]>1:   
    print(start.shape)
    maj_bit, min_bit = bit_filter(start)
    fancy = [i for i, j in enumerate(start[:,0]) if j == min_bit]
    min_collect.append(bit_filter(start)[1])
    start = start[fancy][:,1:]

    if start.shape[0] == 1:
        min_collect.append(list(start)) 
print(min_collect)

co2_scrub = int(func(min_collect),2)
print(co2_scrub)

# %%
result = ox_gen*co2_scrub
print(result)
# %%
