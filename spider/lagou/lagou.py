from urllib.request import urlopen
from urllib.request import Request 
from urllib.parse import  urlencode
from bs4 import BeautifulSoup

# url = 'http://www.lagou.com/jobs/list_python?'
# values = {}
# values['city'] = '杭州'
# values['cl'] = 'false'
# values['fromSearch'] = 'true'
# data = urlencode(values)

url = 'http://www.lagou.com/jobs/positionAjax.json?'
values = {'first': 'false', 'pn': 1, 'kd': 'python'}
headers = {'content-type': 'application/json;charset=UTF-8'}

data = urlencode(values)
request = Request(url, data, headers)
response = urlopen(request)
maxpagenum = json.loads(response.read().decode('utf-8'))['content']['totalPageCount']

