from urllib.request import urlopen
from urllib.request import Request 
from urllib.parse import  urlencode
from bs4 import BeautifulSoup
import json

url = 'http://www.lagou.com/jobs/positionAjax.json?'
headers = {'content-type': 'application/json;charset=UTF-8'}

request = Request(url, headers = headers)
response = urlopen(request)
# bsObj = BeautifulSoup(response.read(), 'lxml')
jobs = json.loads = (response.read().decode('utf-8'))
print(jobs.get('companyId'))