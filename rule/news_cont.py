# coding=utf-8
import re

def news_attitude(t):
    # 新闻利好-中性-利空
    try:
        attitude = re.search(r'class="news_tag news_tag_inlist news_tag(\d)"',t).group(1)
    except Exception as e:
         attitude = 0
    return attitude

def replace_href(t):
    # 去除 a标签 href
    out =re.sub(r'<a href=".*?">','',t).replace('</a>','')
    out =re.sub(r'<a.*?href=".*?">','',out).replace('</a>','')
    # out =re.sub(r'<div class="adhtml">.*?</div>','',out).replace('</a>','')
    # out = out.replace('<div class="phshow" style="display:none">','<div class="phshow">')
    return out
