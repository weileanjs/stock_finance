# coding=utf-8

def source_filter(t):
    '''
    过滤source含有source_list新闻
    '''
    bs = 1
    filter_list = ['同花顺ifind','同花顺中概股公司整理','同花顺数据中心','同花顺深度分析','同花顺综合','同花顺财经','同花顺美股']
    if t.lower() in filter_list:
        bs = 0
    else:
       pass
    return bs
