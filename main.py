import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url ='https://www.binance.com/pl/price/bitcoin'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


try:
    df1 = pd.read_csv('data.csv')
except:
    pass

price = soup.find_all('div', {'class': 'css-12ujz79'})[0].text[2:].replace(',','')
time =datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
df2 = pd.DataFrame([[price,time]],columns =['price','time'])


try:
    df = pd.concat([df1,df2])
    df.to_csv('data.csv')
except:
    df2.to_csv('data.csv')