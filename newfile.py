import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import telegram_send

data = {
  'scan_clause': '( {cash} ( monthly rsi( 14 ) > 60 and weekly rsi( 14 ) > 60 and latest rsi( 14 ) > 60 and 1 day ago  rsi( 14 ) <= 60 and latest volume > 100000 ) ) '
}

with requests.Session() as s:
    r = s.get('https://chartink.com/screener/time-pass-48')
    soup = bs(r.content, 'lxml')
    s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']
    r = s.post('https://chartink.com/screener/process', data=data).json()
    #print(r.json())
    #pd.set_option('display.max_columns', None)
    #pd.set_option('display.max_rows', None)
    df = pd.DataFrame(r['data'])
    #df.to_csv('data.csv', index =False)
    ssList =(df['nsecode'].to_list())
    ss= ('\n'.join(ssList))
    telegram_send.send(messages=[ss])
    
    print(df)