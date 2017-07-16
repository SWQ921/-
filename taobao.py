# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:03:40 2017

@author: dell8
"""

import requests
import re
import pandas as pd
def gethtmltext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return("")

def parsepage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        price = []
        title = []
        for i in range(len(plt)):
            price1=eval(plt[i].split(':')[1])
            title1=eval(tlt[i].split(':')[1])
            price.append(price1)
            title.append(title1)
        return price,title
        
    except:
        print("")
def printgoodslist(ilt):
    tplt ="{:4}\t{:8}\t{:16}"
#    print(tplt.format("序号","价格","商品名称"))
    count =0
    for g in ilt:
        count=count +1 
#        print(tplt.format(count,g[0],g[1]))
def main():
    goods = '短袖'
    depth=2
    start_url='http://s.taobao.com/search?q='+goods
    infolist=[]
    for i in range(depth):
        try:
            url = start_url+'&s='+str(44*i)
            html = gethtmltext(url)
            price,title=parsepage(infolist,html)
            
        except:
            continue
    dc = {'price':list(map(float,price)),'title':title}
    data=pd.DataFrame(dc)
    print(data.sort_values('price'))
    printgoodslist(infolist)
main()
            
            
    