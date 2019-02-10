# -*-coding:utf-8-*-
#requests 用来请求
import requests
#bs4 是 用来提取标签中的内容，比正则简单一些
from bs4 import BeautifulSoup
#pandas用来将所获取到的数据存入excel中
import pandas

newsary = []

for i in range(10):

    #请求这个豆瓣的地址，用res接收请求的结果
    res = requests.get('https://book.douban.com/top250?start=' + str(i * 25))

    #用BeautifullySoup将获取的数据进行解析，解析成了html代码
    soup = BeautifulSoup(res.text, 'html.parser')

    for news in soup.select('.item'):
        person = news.find_all(class_='pl')[1].text.replace(' ', '')
        title = news.select('a')[1].text.replace(' ','')

        jianjie = ""
        try:
            jianjie = news.find_all(class_='inq')[0].text
        except:
            pass;
        name = news.select('p')[0].text
        a = news.select('p')[0].text
        price = a.split('/')[-1]
        time = a.split('/')[-2]
        store = a.split('/')[-3]
        name1 = news.select('p')[0].text.split('/')[:-3][0]
        name2 = ""
        try:
            name2 = "," + news.select('p')[0].text.split('/')[:-3][1]
        except:
                pass;

        newsary.append({'title': title , 'name': name1 + name2 , 'person':person , 'jianjie': jianjie , 'price' : price , 'time' : time , 'store' : store })


newsdf = pandas.DataFrame(newsary)
newsdf.to_excel('doubanbook1.xlsx')


