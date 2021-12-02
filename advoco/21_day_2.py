# %%
# directions = []
horiz = 0
aim = 0
vert = 0

with open('21_day2_i.txt', 'r') as f:
    for line in f:
        dir = line.split()
        if dir[0] == 'forward':
            horiz = horiz + int(dir[1])
            vert = vert + int(dir[1])*aim
        else:
            if dir[0] == 'down':
                aim = aim + int(dir[1])
            else: 
                aim = aim - int(dir[1])
        # print(dir[0], dir[1], horiz, aim, vert)

print(horiz, vert)
print(horiz*vert)

# %%
