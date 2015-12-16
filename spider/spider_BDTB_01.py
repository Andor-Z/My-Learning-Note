__author__ = 'Andor_Z'

import urllib
import urllib.request as ur 
import re

# 百度贴吧爬虫类
class BDTB:

	# 初始化，传入基地址，是否只看楼主的参数
	def __init__(self, baseUrl, seeLZ):
		self.baseURL = baseUrl
		self.seeLZ