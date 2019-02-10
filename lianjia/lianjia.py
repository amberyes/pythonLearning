# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import urllib2

import time
import pandas as pd
time.clock()

address = []

flood = []

follow = []

price = []

for i in range(1,101):
    url = 'https://hz.lianjia.com/ershoufang/xihu/pg'+str(i)+'/'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    for link in soup.find_all('div','address'):
        context = link.get_text()
        address.append(context)
        # for i in address:
        #    print address[0]

    for link in soup.find_all('div','flood'):
        context2 = link.get_text()
        flood.append(context2)

    for link in soup.find_all('div','followInfo'):
        context3 = link.get_text()
        follow.append(context3)

    for link in soup.find_all('div','totalPrice'):
        context4 = link.get_text()
        price.append(context4)
    print (time.clock())
    print '当前正在抓取第'+str(i)+'页'

house = pd.DataFrame({'huxing':address,'address':flood,'follow':follow,'totalprice':price})

huxing_split = pd.DataFrame((x.split('|') for x in house.huxing),
                            index = house.index,columns=['xiaoqu','hux','mianji','chaoxiang',
                                                         'zhaungxiu','dianti',''])
address_split = pd.DataFrame((x.split('-') for x in house.address),
                            index = house.index,columns=['loulishi','dizhi'])
follow_split = pd.DataFrame((x.split('/') for x in house.follow),
                            index = house.index,columns=['following','alreadylooked','fabu'])

house = pd.merge(house,huxing_split,right_index=True,left_index=True)
house = pd.merge(house,address_split,right_index=True,left_index=True)
house = pd.merge(house,follow_split,right_index=True,left_index=True)
house = house.drop(['huxing','address','follow','dianti','loulishi'],axis=1)

house.to_csv('xiaoshan.csv',encoding='gbk',index=False)
print '以上一共收集到'+str(len(house))+'个房源信息'