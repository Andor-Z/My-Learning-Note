import urllib
import urllib.request as ur  
import http.cookiejar as hc

def signin():
    logCookieFile = 'logCookie.txt'
    cookie = hc.MozillaCookieJar(logCookieFile)
    handler = ur.HTTPCookieProcessor(cookie)
    opener = ur.build_opener(handler)
    postdata = urllib.parse.urlencode({'account':'15957166286',
                                 'password':'*********'
                                 })
    b_postdata = postdata.encode('ascii')
    print(postdata)
    signinURL = 'https://www.zhihu.com/#signin'

    # 模拟登录,并把cookie保存到变量
    result = opener.open(signinURL, b_postdata)
    # 保存cookie到文件中
    cookie.save(ignore_discard = True, ignore_expires = True)

    url = 'https://www.zhihu.com/question/35067324#answer-27529133'

    result = opener.open(url)
    print(result.read())

# signin()
# 最后返回 403 Forbidden