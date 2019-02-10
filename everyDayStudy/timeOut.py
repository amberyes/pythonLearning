import urllib
import urllib2

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'zhaofan'
}
data = urllib.urlencode(dict)
#req = urllib2.Request(url=url, data=data, headers=headers)

response = urllib.urlopen(url)
print(response.read().decode('utf-8'))