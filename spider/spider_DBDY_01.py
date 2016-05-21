import requests
from bs4 import BeautifulSoup


class DBDY:

    def __init__(self, db_url):
        self.url = db_url

    def get_page(self):
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'}
        data = requests.get(db_url,headers=headers).content
        return data


    def parse_html(self):
        html = self.get_page()




db_url = 'https://movie.douban.com/top250'
dbdy = DBDY(db_url)
print(dbdy.get_page())