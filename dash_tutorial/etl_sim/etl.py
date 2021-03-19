import pandas as pd
import time

file = '../data_sim/source_sim.csv'

while True:
    df = pd.read_csv(file)    
    df.to_csv('../publ/outp_sim.csv')
    print(df)
    time.sleep(20)
