import http
import http.cookiejar
import urllib.request as ur 

def build_cookie():
    # 声明一个CookieJar对象实例来保存cookie
    cookie = http.cookiejar.CookieJar()

    # HTTPCookieProcessor 创建cookie处理器
    handler = ur.HTTPCookieProcessor(cookie)

    # 通过handler构建opener
    opener = ur.build_opener(handler)

    response = opener.open('http://mm.taobao.com/25115086.htm')

    for item in cookie:
        print('name = '+item.name)
        print('value = '+item.value)


def write_cookie():
    cookie_file = 'cookie.txt'
    # 声明一个MOzillaCookieJar对象来保存cookie,之后写入文件
    cookie = http.cookiejar.MozillaCookieJar(cookie_file)

    # ur库的HTTPCookieProcessor 创建cookie处理器
    handler = ur.HTTPCookieProcessor(cookie)

    opener = ur.build_opener(handler)

    response = opener.open('http://mm.taobao.com/25115086.htm')

    cookie.save(ignore_discard = True, ignore_expires = True)

    # ignore_discard: save even cookies set to be discarded. 
    # 即使cookie将被丢弃也将它保存
    # ignore_expires: save even cookies that have expiredThe file is overwritten if it already exists
    # 如果该文件已经存在,则覆盖原文件写入
