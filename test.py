import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

data = {
  'scan_clause': '( {cash} ( monthly rsi( 14 ) > 60 and weekly rsi( 14 ) > 60 and latest rsi( 14 ) > 60 and 1 day ago  rsi( 14 ) <= 60 and latest volume > 100000 ) ) '
}

with requests.Session() as s:
    r = s.get('https://chartink.com/screener/time-pass-48')
    soup = bs(r.content, 'lxml')
    s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']
    r = s.post('https://chartink.com/screener/process', data=data).json()
    #print(r.json())
    df = pd.DataFrame(r['data'])
    print(df)
