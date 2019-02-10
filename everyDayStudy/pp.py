# -*- coding: UTF-8 -*-
import requests
import json
from lxml import etree
import time

url = 'https://movie.douban.com/subject/1292722/?tag=%E7%BB%8F%E5%85%B8&from=gaia_video'
data = requests.get(url).text
s=etree.HTML(data)
film_name = s.xpath('//*[@id="content"]/h1/span[1]/text()')

film_name=s.xpath('//*[@id="content"]/h1/span[1]/text()')     #电影名
director=s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')  #导演
actor=s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')     #主演
movie_time=s.xpath('//*[@id="info"]/span[15]/text()')         #片长


ds = []
for d in director:
    ds.append(d)

#以列表的形式输出演员
acs = []
for a in actor:
    acs.append(a)
print 'Movie:' + json.dumps(film_name, encoding="UTF-8", ensure_ascii=False)
print 'Director:' + json.dumps(ds, encoding="UTF-8", ensure_ascii=False)
print 'Actors:' + json.dumps(acs, encoding="UTF-8", ensure_ascii=False)
print 'File Length:' + json.dumps(movie_time, encoding="UTF-8", ensure_ascii=False)
