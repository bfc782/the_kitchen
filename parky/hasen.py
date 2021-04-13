#%%
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.parkrun.com.de/hasenheide/results/eventhistory/'

session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept' : 'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.8'}

req = session.get(url, headers=headers)
bs = BeautifulSoup(req.text, 'html.parser')

count = len(bs.find('tbody'))
print(count)

table = bs.find('tbody')

event_dict = dict()


for event in range(count):
    col = table.find_all('tr')[event].find_all('td')
    event_dict[col[0].get_text()]=[col[1],col[2],col[3]]

df = pd.DataFrame(event_dict)

print(df.head())
 





# %%
