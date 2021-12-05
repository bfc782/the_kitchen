# %%
import numpy as np 
from operator import contains

# %%
count = 0
board = []
with open('21_day4_i.txt','r') as f:
    for line in f:
        if count == 0:
            order_dirty = line.split(',')
            order = [int(i) for i in order_dirty]
            count += 1
        else:
            board.append(line.split())
            board = [[int(j) for j in i] for i in board]

# %%
def board_size(x):
    count = 0 
    for i in range(len(x)):
        if i == 0:
            pass
        else:
            if board[i] == []:
                return i-1


# %%
board_dim = board_size(board)
space_shape = board_dim + 1
board_count = len(board) / space_shape # for boards of size 5

# %%
boards = []

# %%
for i in range(1,len(board),space_shape):
    new_board = np.array(board[i:i+board_dim])
    boards.append(new_board)

# %%
check_lists = [] # each board has 2*dim checklists
found = 0

for r in range(board_dim, len(board)): #starts after dim
    new_seq = np.array(order[:r])
    # while found < 1:            
    for i, j in enumerate(boards): # for each board j
        for k, l in enumerate(j[:]): # for each row, l, in board j
            check_list_row = []
            for x in l:
                for y in new_seq:
                    check_list_row.append(x==y)
            if sum(check_list_row)==board_dim:
                check_lists.append(['board:', i, 'row:', k, 'last call_row:', new_seq[-1], 'draw no:', len(new_seq)])
        for m, n in enumerate(j.T[:]): # for each col, n, in board j
            check_list_col = []
            for x in l:
                for y in new_seq:
                    check_list_col.append(x==y)
            if sum(check_list_col)==board_dim:
                check_lists.append(['board:', i, 'col:', m, 'last call_col:', new_seq[-1], 'draw no:', len(new_seq)])

# %%
draws = new_seq
undrawn = []
for i in boards[82][:]: #i is row in array
    for j in i: #j is element in row
        test = []
        for k in draws: # k is drawn number
            test.append(j==k)            
        if sum(test) >0:
            undrawn.append(j)

# %%
sum_undrawn = sum(list(set(undrawn)))
last_draw = check_lists[0][5]

print(sum_undrawn*last_draw)
# %%
