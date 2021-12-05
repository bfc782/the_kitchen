# %%
import numpy as np 
from operator import contains

# %%
count = 0
board = []
# with open('21_day4_i.txt','r') as f:
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
found = 0
count = 0
r = 5
while found == 0:
    # for r in range(board_dim, len(order)): #starts after dim
    r +=1
    new_seq = order[:r]

    for i, j in enumerate(boards): # iterate boards j
        for k, l in enumerate(j[:]): # iterate rows l
            if len([x for x in l if x in new_seq]) == 5:
                print('row', 'draw index:', r, 'last draw:', new_seq[-1], 'board:', i)
                found +=1
                bd_row = boards[i]
                drw_row = new_seq

        for m, n in enumerate(j.T[:]):
            if len([y for y in n if y in new_seq]) == 5:
                print('col', 'draw index:', r, 'last draw:', new_seq[-1], 'board:', i)
                found += 1   
                bd_col = boards[i]
                drw_col = new_seq            


# %%
bd = bd_col
drw = new_seq

undr = []
for i in bd: #row in board
    for j in i: # element in row
        if j not in drw:
            undr.append(j)
# %%
new_seq[-1]*sum(undr)
# %%
