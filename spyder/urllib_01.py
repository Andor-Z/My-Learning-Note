import urllib
import urllib.request as ur


url_baidu = 'http://www.baidu.com'
url_ftp  = 'ftp://example.com/'
username = 'Andor'
password = '0123'
values1 = {"username":username,"password":password}


values = {'name' : 'Andor',  
          'location' : 'zh',  
          'language' : 'Python' } 
url_3 = 'http://www.someserver.com/register.cgi'


data = {}
#data['name'] = 'Andor'
#data['location'] = 'zh'
#data['language'] ='Python'
data['name'] = 'WHY'  
data['location'] = 'SDU'  
data['language'] = 'Python'
url_4 = 'http://www.example.com/example.cgi' 
def ex1(url):
	req = ur.Request(url)
	response = ur.urlopen(req)
	the_page = response.read()
	print(the_page)

def ex2(url, values):
	'''
	POST数据传输方式
	通常会有'副作用'，会由于某种途径改变系统状态

	2中的urllib.urlencode变成urllib.parse.urlencode
	并且在进行数据传输时需要对已经urlencode的数据使用data.encode('encoding')方法编码
	Python文档中是这么说的：
	urlencode是把一个str或者bytes的对象，编码成一个percent-encodedASCII的文本字符串，如果这个字符串需要作为一个urlopen()函数POST传输的data的话，它还需要再进行一次编码成bytes，否则，将返回一个TypeError

	'''
	# 对表单数据进行编码
	data = urllib.parse.urlencode(values)


	##对data进行解码
	binary_data = data.encode('utf-8')


	# 发送url请求的同时传data表单
	req = ur.Request(url, binary_data)
	# 接收反馈信息
	response = ur.urlopen(req)
	the_page = response.read()
	print(the_page)

def ex3(url, data):
	'''
	GET方式的请求
	直接把参数写到网址上，直接构建了一个带参数的URL

	'''
	url_values = urllib.parse.urlencode(data)
	print(url_values)
	full_url = url + '?' + url_values
	req = ur.Request(full_url)
	response = ur.urlopen(req)
	print(response)





#ex3(url_4, data)

#ex2(url_3, values)
#ex1(url_ftp)