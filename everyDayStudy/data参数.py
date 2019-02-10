import urllib


data = urllib.urlencode({'word': 'hello'})
print(data)
response = urllib.urlopen('http://httpbin.org/post', data=data)
print(response.read())