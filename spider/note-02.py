import urllib
import urllib.request as ur

def spider_01():
    '''Proxy 代理设置
    '''
    enable_proxy = True 
    proxy_handler = urllib.request.ProxyHandler({'http' : 'http://some-proxy.com:8080'})
    null_proxy_handler = ur.ProxyHandler({})
    if enable_proxy:
        opener = ur.build_opener(proxy_handler)
    else:
        opener = ur.build_opener(null_proxy_handler)
    ur.install_opener(opener)

def spider_02():
    ''' 使用HTTP的PUT和DELECT方法（http协议有六种请求方法，get,post,put,delete,head,options）
    '''
    request = ur.Request(uri, data=data)
    request.get_method = lambda: 'PUT' # or 'DELETE'
    response = ur.urlopen(request)

def spider_03():
    '''使用DebugLog
    '''
    import urllib2
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.baidu.com')
