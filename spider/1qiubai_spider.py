import urllib
import urllib.request
import re
import time



def spider_qb_1():
	page = 1
	url = 'http://www.qiushibaike.com/hot/page/' + str(page)
	
	try:
		request = urllib.request.Request(url )
		response = urllib.request.urlopen(request)
		print(response.read())
	except urllib.error.URLError as e:
		#3中URLError归到urllib.error中了
		if hasattr(e, 'code'):
			print(e.code)
		if hasattr(e, 'reason'):
			print(e.reason)
	'''
	由于缺少headers 故出错
	'''


def spider_qb_2():
	page = 1
	url = 'http://www.qiushibaike.com/hot/page/' + str(page)
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
	header = {'User-Agent': user_agent}
	try:
		request = urllib.request.Request(url, headers = header )
		response = urllib.request.urlopen(request)
		print(response.read())
	except urllib.error.URLError as e:
		#3中URLError归到urllib.error中了
		if hasattr(e, 'code'):
			print(e.code)
		if hasattr(e, 'reason'):
			print(e.reason)

	'''
	加上headers验证，打印出HTML代码
	'''

def spider_qb_3():
	page = 1
	url = 'http://www.qiushibaike.com/hot/page/' + str(page)
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
	header = {'User-Agent': user_agent}
	try:
		request = urllib.request.Request(url, headers = header )
		response = urllib.request.urlopen(request)

		content = response.read().decode('utf-8')

		pattern = re.compile('"author clearfix".*?<h2>(.*?)</h2>.*?"content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?number">(.*?)</i>',re.S)

		items = re.findall(pattern, content)
		print(items)
		for item in items:

			haveImg = re.search('img', item[3])
			
			if haveImg == None:
				for i in range(len(item)):

					if i == 2:
						print(time.strftime('%Y-%m-%d %H:%M',time.localtime(int(item[i]))))
					else:
						print(item[i])

					


		#print(response.read())
	except urllib.error.URLError as e:
		#3中URLError归到urllib.error中了
		if hasattr(e, 'code'):
			print(e.code)
		if hasattr(e, 'reason'):
			print(e.reason)

	
	#print(content)

	# 这个正则表达式中，取了组，分别代表 发布人、发布时间、发布内容、附加图片、 点赞数
	# .* 匹配任意无限多个字符 ，加上? 表示非贪婪模式，即尽可能段的做匹配
	pattern0 = re.compile('<div.*?content">(.*?)<!--(.*?)-->',re.S)  
	#只取正文 和时间  但是时间只取出了一个数字

	pattern1 = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)<!--(.*?)-->',re.S)
	pattern1_1 = re.compile('<h2>(.*?)</h2>.*?<div.*?content">(.*?)<!--(.*?)-->',re.S)
	# 只取 作者 正文  时间  但是当没有作者时，这段糗百就取不到了

	pattern2 = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)<!--(.*?)-->.*?</div>.*?<img src=(.*?)alt=',re.S)
	# 取 作者 正文 时间 图片链接 ，但是当原文没有其中任何一样时，这段糗百就取不到
	pattern3 = re.compile('"author clearfix".*?<h2>(.*?)</h2>.*?"content">(.*?)<!--(.*?)-->.*?"thumb".*?src=(.*?) alt=.*?"number">(.*?)</i>',re.S)
	# 取 作者 正文 时间 图片链接 ，但是当原文没有其中任何一样时，这段糗百就取不到
	


	
	
	
	
		
spider_qb_3()

#pattern = re.compile('"author clearfix".*?<h2>(.*?)</h2>.*?"content">(.*?)<!--(.*?)-->.*?number">(.*?)</i>',re.S)



















