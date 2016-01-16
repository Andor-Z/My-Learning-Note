import urllib
import urllib.request as ur
import re


class Tool:

    '''
    处理页面标签类
    '''
    # 去除img标签
    removeImg = re.compile('<img.*?>')

    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')

    # 把换行标签替换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    
    # 把换行符或者双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')

    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')

    # 将段落开头替换为 \n 加2空格
    replacePara = re.compile('<p.*?>')

    # 剔除其余标签
    removeExtraTag = re.compile('<.*?>')
    
    def repalce(self, x):
        x = re.sub(self.removeAddr,"", x)
        x = re.sub(self.removeImg, "", x)
        
        x = re.sub(self.replaceBR, '\n', x)
        x = re.sub(self.replaceLine, '\n', x)
        x = re.sub(self.replacePara, '\n  ', x)
        x = re.sub(self.replaceTD, '\t', x)
        # 注意 剔除其他标签要放到最后
        x = re.sub(self.removeExtraTag, "", x)

        return x.strip()


# 百度贴吧爬虫类
class BDTB:

    # 初始化，传入基地址，是否只看楼主、是否看楼层信息的参数

    def __init__(self, baseUrl, seeLZ, floorTag):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()

        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层编号，初始为1
        self.floor = 1
        # 默认标题，若未成功获取标题，则使用默认标题
        self.defaultTitle = '百度贴吧'
        # 是否写入楼层分隔符的标记
        self.floorTag = floorTag

    # 传入页码，获取该页的代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            r = response.read().decode('utf-8')
            return r
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('连接百度贴吧失败，错误原因：', e.reason)
                return None

    def getTitle(self, page):
        '''
        获取帖子标题
        page 是getPage函数返回的响应

        '''
        pattern = re.compile('<h3 class=.*?title="(.*?)" style', re.S)
        result = re.search(pattern, page)
        if result:
            #print(result.group(1))
            return(result.group(1).strip())
        else:
            return None

    def getPageNum(self, page):
        '''
        提取帖子页数
        '''
        
        pattern = re.compile(
            '<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            #print(result.group(1))
            return(result.group(1).strip())

        else:
            return None

    def getContent(self, page):
        '''
        提取正文内容
        获取每层楼的内容，传入页面内容
        '''
        #page = self.getPage(1)
        pattern = re.compile('<cc>.*?_post_content ">(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            '''
            对文本进行去除标签处理，同时前后加入换行符
            '''
            content = '\n' + self.tool.repalce(item) + '\n'
            contents.append(content)
        #print(contents)
        return contents

    def setFileTitle(self, title):
        # 若标题不为空None，则成功获取到标题
        if title is not None:
            self.file = open(title + '.txt', 'w+')
        else:
            self.file = open(self.defaultTitle + '.txt', 'w+')

    def writeData(self,contents):
        
        for item in contents:
            if self.floorTag == '1':
                floorLine = '\n' + str(self.floor) + '楼------------------------------------------------\n'
                #print(floorLine)
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1
            
           #else:


    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print('URL已失效或者无法提取贴子页面数信息')
            return None
        try:
            print('该贴子共有' + str(pageNum) +'页')
            for i in range(1, int(pageNum) +1):
                print('正在写入'+ str(i) + '页')
                page = self.getPage(i)
                contents = self.getContent(page)
                
                self.writeData(contents)
        except IOError as e:
            print('写入异常，原因：' + e.message)
        finally:
            self.file.close()
            print('完成')


        

            



print('请输入百度贴吧帖子代号')

baseURL = 'http://tieba.baidu.com/p/' + str(input('http://tieba.baidu.com/p/'))
seeLZ = input('是否只获取楼主发言，“是”请输入1，“否”请输入0\n')
floorTag = input('是否写入楼层信息，是 请输入1，否 请输入0\n')
bdtb = BDTB(baseURL, seeLZ, floorTag)

bdtb.start()
