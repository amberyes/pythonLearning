import urllib

response = urllib.urlopen('https://movie.douban.com/top250')
print(response.read().decode('utf-8'))