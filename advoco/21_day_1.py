# %%
import re
depths = []
count = 0

with open('21_day1_i.txt', 'r') as f:
    for line in f:
        if depth_before == None:
            pass
        else:
            depth_before = depth_now
            depth_now = int(re.sub('[\D]', '', line))
            depths.append((depth_now, depth_before))
            if depth_now > depth_before:
                count += 1
print(count)

# %%
from collections import deque

depths = deque(maxlen=4)
count = 0

with open('21_day1_i.txt', 'r') as f:
    for line in f:
        depth_now = int(re.sub('[\D]', '', line))
        depths.append(depth_now)
        if len(depths) < 4:
            pass
        else:
            if sum(list(depths)[1:]) > sum(list(depths)[:3]):
                count += 1
print(count)

# %%
