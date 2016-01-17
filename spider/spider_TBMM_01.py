import urllib
import urllib.request as ur
import re


class TBMM:
    
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        #self.tool = 

    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        #print(url)
        request = ur.Request(url)
        response = ur.urlopen(request)
        return response.read().decode('gbk')

    def getContents(self,pageIndex):
        '''
        获取索引界面所有MM的信息，list格式
        0是MM域名，1是MM头像地址，2是MM姓名，3是MM年龄，4是MM地址
        '''
        page = self.getPage(pageIndex)
        
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            contents.append([item[0], item[1], item[2], item[3],item[4]])
        return contents

    def getDetailPage(self,infoURL):
        '''
        得到MM个人页面的代码
        '''
        infoURL = 'http:'+infoURL
        request = ur.Request(infoURL)
        response = ur.urlopen(request)
        #print(response.read().decode('gbk'))
        return response.read().decode('gbk')

    def getBrief(self, page):
        '''
        获取个人文字简介
        '''
        #暂时不做，现在使用了“爱可秀的”什么东西，导致文字不集中个人简介过于麻烦
        #pattern = re.compile('')

    def getAllImg(self,page):
        pattern = re.compile('<img style.*?src="(.*?)".*?',re.S)
        images = re.findall(pattern, page)
        return(images)
        
    
    def saveImgs(self,images,name):
        number = 1
        for url in images:
            print()

    def saveImg(self, imgURL, fileNmae):
        '''
        传入图片地址，文件名，保存单张图片
        '''
        u = ur.urlopen(imgURL)
        data = u.read()
        f = open(fileNmae,'wb')
        f.write(data)
        f.close()

    def saveBrief(self, content, name):
        fileNmae = name + '/' +name +'.txt'
       
    def savePageInfo(self, pageIndex):
        '''
        将一页MM的信息保存
        '''
        contents = self.getContents(pageIndex)
        for item in contents:
            print('发现一名模特，名字叫'+item[2]+'，芳龄'+item[3] + '，她在'+ item[4])
            print('她的个人域名是:' + item[0])
            print('正在保存'+ item[2]+ '的信息')
            # MM域名的URL
            detailURL = item[0]
            # 获取MM个性域名页面的代码
            detailPage = self.getDetailPage(detailURL)
            # 获取个人简介
            #brief = self.




tbmm = TBMM()
page = tbmm.getDetailPage('//mm.taobao.com/jxyueyue')
images = tbmm.getAllImg(page)
image = 'http:'+images[8]
tbmm.saveImg(image,'2')

    
        