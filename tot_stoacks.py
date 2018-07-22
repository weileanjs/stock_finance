import tushare as ts
import pandas as pd
import time
import datetime
from to_mysql import insert_tot_stocks
def get_tot_stocks():
    df = ts.get_today_all()
    print(df.shape)
    # df = pd.read_csv('xxx.csv',encoding = 'gb18030')
    name_list = df['name'].tolist()
    code_list = df['code'].tolist()
    market = []
    for code in code_list:
        if int(code) > 599999:
            market.append('sh')
        else:
            market.append('sz')
    df['market'] = market
    df.to_csv('xxx.csv')
    for name,code,market_ in zip(name_list,code_list,market):
        createtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        code = ('00000'+str(code))[-6:]
        print(name,code,market_)
        insert_tot_stocks(name,code,market_,createtime)



get_tot_stocks()