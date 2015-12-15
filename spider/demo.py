response = urllib.request.urlopen(web)
print(response.read())


python3中urllib2变成了urllib.request

urlopen(url, data, timeout)

data 是访问url时需要传送的数据
timeout 设置超时时间

##构造Request

import urllib
web = input('please enter url:')
request = urllib.request.Request(web)
response = urllib.request.urlopen(request)
print(response.read())

##post 和get数据传送
###post
python3中urllib.urlencode变成了urllib.parse.urlencode

import urllib
username = input('please enter username:')
password = input('please input password:')
url = input('please enter url:')

values = {"username":username,"password":password}
data = urllib.parse.urlencode(values)     #利用urllib.parse.urlencode方法将字典编码
request = urllib.request.Request(url, data)
response = urllib.request.urlopen(request)
print(response.read())


###GET方式
import urllib
username = input('please enter username:')
password = input('please input password:')
url = input('please enter url:')

values = {}
values['username'] = username
values['password'] = password
data = urllib.parse.urlencode(values)
geturl = url + '?' + data
request = urllib.request.Request(geturl)
response = urllib.request.urlopen(request)
print(response.read())


#Python爬虫入门4——urllib库的高级应用
##Headers
###Headers中的agent请求的身份, 

import urllib
password = input('please input password:')

url = 'http://www.zhihu.com/#signin'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
values = {}
values['username'] = '1245349234@qq.com'
values['password'] = password
headers = {'User-Agent' : user_agent}
headers['Referer']= 'http://www.zhihu.com'

data = urllib.parse.urlencode(values).encode(encoding = 'UTF8') ##!!!加了encode方法
request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)
page = response.read()


###cookielib  在python3中为 http.cookiejar


import urllib.request  as ur #2中的urllib2
import http.cookiejar  as hc #2中的cookielib
url = input('please enter url:')

cookie = hc.CookieJar()  #声明一个cookjar对象实例来保存cookie
handler = ur.HTTPCookieProcessor(cookie)  #利用urllib.request中的HTTPCookieProcessor来创建cookie处理器
opener = ur.build_opener(handler)
response = opener.open(url)
for item in cookie:
	print('Name = ' + item.name)
	print('Value = ' + item.values)


#将cookie保存到文件中
import urllib.request  as ur #2中的urllib2
import http.cookiejar  as hc #2中的cookielib
url = input('please enter url:')

filename = 'cookie.txt'
cookie = hc.MozillaCookieJar(filename)
handler = ur.HTTPCookieProcessor(cookie)
opener = ur.build_opener(handler)
response = opener.open(url)
cookie.save(ignore_discard = True, ignore_expires = True)


#从文件中获取cookie并访问
