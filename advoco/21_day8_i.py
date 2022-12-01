# %%
EASY = [None, None, 1, 7, 4, '235', '069', 7, 8]


# %%

inp_list = []
out_list = []

with open('21_day8_i.txt', 'r') as f:
    for ind, line in enumerate(f):
        inp = line.split('|')[0]
        out = line.split('|')[1]
        inp_ind = inp.split()
        out_ind = out.split()
    
        inp_list.append(inp_ind)
        out_list.append(out_ind)

        # inp_dec = [EASY[len(j)] for j in _ for i in inp_list]
        # out_dec = [EASY[len(j)] for j in _ for i in out_list]
        # easy_map = easy_map + [[ind, i, j] for i in inp_ind \
            # for j in out_ind if {k for k in i} == {l for l in j}]

# %%
elemap = {'t': [0, 2, 3, 5, 6, 7, 8, 9],
        'b': [0, 2, 3, 5, 6, 8, 9],
        'm': [2, 3, 4, 5, 6, 8, 9],
        'ur': [0, 1, 2, 3, 4, 7, 8, 9], 
        'ul': [0, 4, 5, 6, 8, 9], 
        'br': [0, 1, 3, 4, 5, 6, 7, 8, 9],
        'bl': [0, 2, 6, 8]}


[v for k, v in elemap.items()]
# %%
num_to_elem = {}
for num in range(10):
    for elem, v in elemap.items():
        if not num_to_elem.get(str(num)):
            num_to_elem[str(num)] = set()
        if num in v:
            num_to_elem[str(num)].add(elem)
    
# %%
from itertools import combinations
comb = []
x = combinations([k for k, _ in num_to_elem.items()], 2)
for i, j in list(x):
    test1 = num_to_elem[i] - num_to_elem[j]
    test2 = num_to_elem[j] - num_to_elem[i]
    if len(test1) == 1:
        comb.append((test1, i, j))
    if len(test2) == 1:
        comb.append((test2, j, i))

# %%
sort_elems = lambda c: ''.join(sorted([i for i in c]))
[sort_elems(i) for i in inp_ind]


# %%
def decode(x):

    codes = [None, None, None, None, None, None, None, None, None, None]
    sig_map = {'632': 0, 
                '521': 2, 
                '532': 3, 
                '531': 5, 
                '631': 6, 
                '642': 9, 
                }

    for i in x:
        if len(i) == 2:
            codes[1] = i
        elif len(i) == 3:
            codes[7] = i
        elif len(i) == 4:
            codes[4] = i
        elif len(i) == 7:
            codes[8] = i
    
    for j in x:
        if (len(j) == 5) | (len(j) == 6):
            signature = str(len(j)) \
                + str(len([k for k in codes[4] if k in j])) \
                    + str(len([k for k in codes[1] if k in j]))
            if signature == '542':
                return j

            codes[sig_map[signature]] = j 
        else:
            signature = 'not >= 5'

    codes = [''.join(sorted(i)) for i in codes]

    code_dict = {k: v for v, k in enumerate(codes)}
        
    return code_dict #signature #sig_map.get(signature)

    return codes

    for i in x:
        r1 = codes[1][0]
        r2 = codes[1][1]
        if len(i) == 6:
            if (r1 not in i) | (r2 not in i):
                codes[6] = i
        if len(i) == 5:
            if (r1 in i) & (r2 in i):
                codes[3] = i
    
    five_six = [i for i in x if (i != codes[3]) & (len(i) >= 5)]
    for i in five_six:
        common = []
        for j in codes[4]:
            if j in i:
                common.append(j)
            if (len(common) == 2) & (len(i) == 5):
                codes[2] = i
            elif (len(common) == 3) & (len(i) == 5):
                codes[5] = i
            elif (len(common) == 3) & (len(i) == 6) & (i != codes[6]):
                codes[0] = i
            elif (len(common) == 4) & (len(i) == 6):
                codes[9] = i
    
    codes = [''.join(sorted(i)) for i in codes]

    code_dict = {k: v for v, k in enumerate(codes)}

    return code_dict

# %%
code_list = []
for i in inp_list:
    code_list.append(decode(i))

# %%

decode_all = []
for ix, codes in enumerate(out_list):
    sorted_codes = [''.join(sorted(j)) for j in codes]
    decode_curr = []
    for j in sorted_codes:
        decode_curr.append(code_list[ix][j])
    # print(decode_curr)
    decode_all.append(decode_curr)
# %%
for i in decode_all:
    for j in i:
        ''.join(str(j))

# %%
all_combs = []
for i in decode_all:
    concat = ''
    for ix, j in enumerate(i):
        concatable_num = str(j)
        concat = concat + concatable_num
    combs = int(concat)
    all_combs.append(combs)
# %%
sum(all_combs)
# %%
