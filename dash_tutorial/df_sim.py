import pandas as pd
import time
import random

mydict = dict()
nextdict = ''
mylist = []
str_s, str_e = 65,91

init_df = 0

while True: 
    for i in range(3):
        next_input = chr(random.choice(list(range(str_s,str_e))))
        mylist = random.sample(range(0,1023),3)
        mydict[str(next_input)] = mylist
        mylist = []
    
    nextdict = mydict
#    print(nextdict)
    mydict = dict()
    df = pd.DataFrame(nextdict)
    df.to_csv('./data_sim/source_sim.csv')
    time.sleep(5)
