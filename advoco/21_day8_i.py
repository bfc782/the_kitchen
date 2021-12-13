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

        inp_dec = [EASY[len(j)] for j in i for i in inp_list]
        out_dec = [EASY[len(j)] for j in i for i in out_list]
        # easy_map = easy_map + [[ind, i, j] for i in inp_ind \
        #     for j in out_ind if {k for k in i} == {l for l in j}]

# %%
