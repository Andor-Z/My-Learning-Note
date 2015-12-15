__author__ = 'Andor_Z'
import urllib
import urllib.request as ur 
import re
import time
import _thread    #2 中使用 import thread

#糗百爬虫类
class QSBK:

	# 初始化方法， 定义一些变量
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
		# 初始化headers
		self.headers = {'User-Agent' : self.user_agent}

		# 存放段子的变量，每一个元素是每一页的段子们
		self.stories = []

		# 存放程序是否继续运行的变量
		self.enable = False


	# 传入某页的索引获得页面代码
	def getPage(self, pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			request = urllib.request.Request(url, headers = self.headers)
			response = urllib.request.urlopen(request)
			# 将页面转化为UTF-8编码
			pageCode = response.read().decode('utf-8')
			return pageCode

		except urllib.error.URLError as e:
			if hasattr(e, 'reason'):
				print(u'连接糗百失败，错误原因：', e.reason)


	# 传入某页代码，返回本页不带图片的段子列表
	def getPageItems(self, pageIndex):
		pageCode = self.getPage(pageIndex)
		if  pageCode is None: # 原语句为 if not pageCode
			print('页面加载失败')
			return None
		pattern = re.compile('"author clearfix".*?<h2>(.*?)</h2>.*?"content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?number">(.*?)</i>',re.S)
		items = re.findall(pattern, pageCode)
		# 存储每页的段子
		pageStories = []
		for item in items:
			# 是否含有图片
			haveImg = re.search('img', item[3])
			if haveImg == None:
				#item[0]是作者 1是类容 2是发布时间 3是图片，但是会过滤 4是点赞数
				for i in range(len(item)):
					# 替换换行符
					replaceBR = re.compile('<br/>')
					if i == 1:
						text = re.sub(replaceBR, '\n', item[i])
					elif i == 2:
						time_a = time.strftime('%Y-%m-%d %H:%M',time.localtime(int(item[i])))
				pageStories.append([item[0].strip(),text.strip(),time_a.strip(),item[4].strip(),])
		return pageStories

	# 加载并提取页面的类容，加入到列表中	
	def loadPage(self):
		# 如果当前未看的页数少于2页，则加载新一页
		if self.enable ==True:
			if len(self.stories) < 2:
				# 获取新一页
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					# 将该页的段子放到全局中
					self.stories.append(pageStories)
					self.pageIndex += 1

	def getOneStory(self, pageStories, page):
		# 遍历一页的段子
		for story in pageStories:
			# 等待用户输入
			input_in = input()
			# 每当输入回车一次，判断一下是否需要加载新页面
			self.loadPage()
			# 如果输入Q则程序结束
			if input_in == 'Q':
				self.enable = False
				return 
			print(u'第%d页\t发布人：%s\t发布时间：%s\t 赞：%s\n%s' %(page, story[0], story[2],story[3], story[1]))

	# 开始
	def start(self):
		print('正在读取糗百， 按回车查看新段子，Q退出')
		# 使程序变量为True，使程序可以运行
		self.enable = True
		# 加载一页
		self.loadPage()
		# 局部变量 控制当前读到第几页
		nowPage = 0
		while self.enable:
			if len(self.stories)>0:
				# 让pageStories 从全局list self.stories 中获取一页的段子
				pageStories = self.stories[0]
				# 当前读到的页面数加一
				nowPage += 1
				# 因为已经取出，将全局变量中的第一个元素删除
				del self.stories[0]
				# 输出
				self.getOneStory(pageStories, nowPage)



s = QSBK()
s.start()



				

