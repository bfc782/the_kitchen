# %%
OPP = ['A', 'B', 'C']
ME = ['X', 'Y', 'Z']

mapping = {
        'left': {'A': 'Rock',  
                    'B': 'Paper',  
                    'C': 'Scissors', 
            },
        'right': {'X': 'Rock',
                    'Y': 'Paper',
                    'Z': 'Scissors',
            }
        }

def get_score(hands, mapping=mapping):
    opphand, myhand = hands
    if mapping['left'][opphand] == mapping['right'][myhand]:
        return 3

# %%
get_score(('A', 'X'))


# %%
