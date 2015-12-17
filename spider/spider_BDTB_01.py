__author__ = 'Andor_Z'

import urllib
import urllib.request as ur 
import re

# 百度贴吧爬虫类
class BDTB:

	# 初始化，传入基地址，是否只看楼主的参数
	def __init__(self, baseUrl, seeLZ):
		self.baseURL = baseUrl
		self.seeLZ = '?see_lz=' + str(seeLZ)
		


	# 传入页码，获取该页的代码
	def getPage(self, pageNum):
		try:
			url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
			request = urllib.request.Request(url)
			response = urllib.request.urlopen(request)
			#print(response.read().decode('utf-8'))
			r = response.read().decode('utf-8')
			return r
		except urllib.error.URLError as e:
			if hasattr(e, 'reason'):
				print('连接百度贴吧失败，错误原因：', e.reason)
				return None


	def getTitle(self):
		'''
		获取帖子标题

		'''
		page = self.getPage(1)
		pattern = re.compile('<h3 class=.*?title="(.*?)" style', re.S)
		result = re.search(pattern, page)
		if result:
			print(result.group(1))
			print(result.group(1).strip())
		else:
			return None




	def getPageNum(self):
		'''
		提取帖子页数
		'''
		page = self.getPage(1)
		pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
		result = re.search(pattern, page)
		if result:
			print(result.group(1))

		else:
			return None


	def getContent(self):
		'''
		提取正文内容
		'''
		page = self.getPage(1)
		pattern = re.compile('<cc>.*?_post_content ">(.*?)</div>', re.S)
		result = re.findall(pattern, page)
		for item in result:
			print(item)






class Tool:
	'''
	处理页面标签类
	'''
	











baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
#b = bdtb.getPage(1)
#b = bdtb.getPageNum()
bdtb.getContent()