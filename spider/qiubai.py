import urllib
import urllib.request as ur

page = 1
url = 'http://www.qiushibaike.com/hot/page' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
headers = {'User-Agent' : user_agent}
try:
	request = ur.Request(url, headers = headers)
	response = ur.urlopen(request)
	#print(response.read())
except urllib.error.URLError as e:  #3中URLError归到urllib.error中了
	if hasattr(e, 'code'):
		print(e.code)
	if hasattr(e,'reason'):
		print(e.reason)

import re
content = response.read().decode('utf-8')
pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
items = re.findall(pattern, content)
for item in items:
	print(item[0],item[1], item[2], item[3],item[4])

