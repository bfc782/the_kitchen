# %%
import re
collections = []
collected = []

with open('22_day01.txt', 'r') as f:
    for line in f:
        line = re.sub('[\n]', '', line)
        if line != '':
            line = int(line)
            collected.append(line)# += int(line)
        else:
            collections.append(collected)
            collected = []

# %%
collect_sums = [sum(i) for i in collections]
# %%
max(collect_sums)
# %%
