# %%
import re 
with open('22_day04.txt', 'r') as f:
    flags = []
    for ix, line in enumerate(f):
        # if ix < 2:
        x = line.split(',')

        # x = [re.sub('[\n]', '', i) for i in x]
        # x = [re.sub('[-]', ':', i) for i in x]
        x = [re.findall('[\d]+', i) for i in x]
        # print(x)
        x = [[int(j) for j in i] for i in x]
        [a, b] = x 
        a = list(range(a[0], a[1] + 1))
        b = list(range(b[0], b[1] + 1))

        cond = any([i in b for i in a]) | any([i in a for i in b])
        flags.append(cond)
        
# %%
sum(flags)
# %%
