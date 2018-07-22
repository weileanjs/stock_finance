# coding=utf-8

def tit_filter(t):
    '''
    过滤title含有filter_list新闻
    '''
    bs = 1
    filter_list = ['融资融券','level-2','level2','大宗交易','龙虎榜','同花顺智能选股']
    for i in filter_list:
       if i in t.lower():
            bs = 0
            break
       else:
           pass
    return bs
