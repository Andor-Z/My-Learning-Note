import http.cookiejar
import urllib.request as ur 

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
