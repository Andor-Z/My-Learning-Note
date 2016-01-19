import urllib.request as ur
import http
import http.cookiejar

# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()

# HTTPCookieProcessor 创建cookie处理器
handler = ur.HTTPCookieProcessor(cookie)

# 通过handler构建opener
opener = ur.build_opener(handler)

response = opener.open('http://www.baidu.com')

for item in cookie:
    print('name = '+item.name)
    print('value = '+item.value)