import requests
import json
from config import get_header
from to_mysql import get_stock_info,insert_stock_basics
from multiprocessing import Pool
import datetime
import tushare
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')




def get_basics(stock_info):
    base_url = 'https://xueqiu.com/stock/f10/cfstatement.json?symbol={0}&page=1&size=199'
    code_mk = stock_info['market']+stock_info['code']
    req = requests.get(base_url.format(code_mk),headers=get_header())
    json_data = json.loads(req.text)['list']
    for i in json_data:
        for k,v in i.items():
            print(k,v)
        print('**********************************')
        # stock_code = stock_info['code']
        # report_date = i['reportdate']
        # mainbusiincome = i['mainbusiincome']
        # mainbusiprofit = i['mainbusiprofit']
        # totprofit = i['totprofit']
        # netprofit = i['netprofit']
        # totalassets = i['totalassets']
        # totalliab = i['totalliab']
        # totsharequi = i['totsharequi']
        # basiceps = i['basiceps']
        # naps = i['naps']
        # opercashpershare = i['opercashpershare']
        # peropecashpershare = i['peropecashpershare']
        # operrevenue = i['operrevenue']
        # invnetcashflow = i['invnetcashflow']
        # finnetcflow = i['finnetcflow']
        # chgexchgchgs = i['chgexchgchgs']
        # cashnetr = i['cashnetr']
        # cashequfinbal = i['cashequfinbal']
        # createtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(stock_code, report_date)
        # insert_stock_basics(stock_code, report_date, mainbusiincome, mainbusiprofit, totprofit, netprofit, totalassets,
        #                     totalliab, totsharequi, basiceps, naps, opercashpershare, peropecashpershare, operrevenue,
        #                     invnetcashflow, finnetcflow, chgexchgchgs, cashnetr, cashequfinbal,createtime)


get_basics({'code':'600023','market':'sh'})

# if __name__ == '__main__':
#     stock_info_list = get_stock_info()
#     pool = Pool(processes=3)
#     pool.map(get_basics,stock_info_list)
#     pool.close()
#     pool.join()
