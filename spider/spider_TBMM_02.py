import urllib
import urllib.request as ur
import re
import os

class TBMM:
    
    def __init__(self,sPath):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.sPath = sPath



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

    def saveBrief(self, content, name):
        fileNmae = name + '/' +name +'.txt'

    def getAllImg(self,page):
        pattern = re.compile('<img style.*?src="(.*?)".*?',re.S)
        images = re.findall(pattern, page)
        return(images)
        
    
    def saveImgs(self,images,name):
        '''
        保存一个淘宝MM她个人域名下的所有展示图片
        '''
        number = 1
        print('发现',name,'共有',len(images),'张图片')
        for imgURL in images:
            #splitPath = imageURL.split('.')
            #fTail = splitPath.pop()
            #if len(fTail) > 3:
                #fTail = "jpg"
            # 原教程中这几句话不太理解
            path = self.sPath + '\\'+name
            os.chdir(path)
            fileName = str(number) + '.jpg'
            imgURL = 'http:'+imgURL
            try:
                self.saveImg(imgURL,fileName)

            except urllib.error.HTTPError as e:
                print(fileName,e.reason)
            number += 1
            
    def saveIcon(self, iconURL, name):
        path = sPath + '\\'+name
        os.chdir(path)
        fileName = name +'_icon'+ '.jpg'
        iconURL ='http:' + iconURL
        try:
            self.saveImg(iconURL,fileName)

        except urllib.error.HTTPError as e:
            print(fileName,e.reason)



    def saveImg(self, imgURL, fileNmae):
        '''
        传入图片地址，文件名，保存单张图片
        '''
        u = ur.urlopen(imgURL)
        data = u.read()
        f = open(fileNmae,'wb')
        f.write(data)
        f.close()

    def mkMMdir(self,path):
        '''
        创建mm个人的文件
        '''
        isExists = os.path.exists(path)
        if isExists:
            print('名为',path,'的文件夹已经存在')
        else:
            os.mkdir(path)
            print('正在创建名为',path,'的文件夹')

       
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
            # 获取所有图片列表
            images = self.getAllImg(detailPage)
            imgNum = len(images)
            if imgNum == 0:
                print('未能获取到这个MM的个人域名和图片信息，请检查')
            else:
                #创建mm个人的文件夹
                path = self.sPath + '\\'+item[2]
                self.mkMMdir(path)
                # 保存头像
                self.saveIcon(item[1],item[2])
                # 保存mm的图片
                self.saveImgs(images, item[2])

    def savePagesInfo(self, start, end):
        '''
        传入起止页面，获取MM图片
        '''
        for i in range(start,end+1):
            print('正在查找第',i,'页')
            self.savePageInfo(i)




sPath = 'd:\mm'
tbmm = TBMM(sPath)
tbmm.savePagesInfo(2,3)


'''
正在查找第 2 页
发现一名模特，名字叫李喵喵，芳龄26，她在上海市
她的个人域名是://mm.taobao.com/45834230.htm
正在保存李喵喵的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫悦小舞，芳龄26，她在北京市
她的个人域名是://mm.taobao.com/91442126.htm
正在保存悦小舞的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫夏欢欢，芳龄26，她在杭州市
她的个人域名是://mm.taobao.com/272536951.htm
正在保存夏欢欢的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫赵颖，芳龄26，她在广州市
她的个人域名是://mm.taobao.com/63153008.htm
正在保存赵颖的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫姬嘉琳，芳龄28，她在广州市
她的个人域名是://mm.taobao.com/319426092.htm
正在保存姬嘉琳的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫邝萃莉，芳龄25，她在广州市
她的个人域名是://mm.taobao.com/646858747.htm
正在保存邝萃莉的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫吴若梵，芳龄27，她在杭州市
她的个人域名是://mm.taobao.com/276439081.htm
正在保存吴若梵的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫熊仔欣，芳龄4，她在广州市
她的个人域名是://mm.taobao.com/717492986.htm
正在保存熊仔欣的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫阿朵拉，芳龄26，她在上海市
她的个人域名是://mm.taobao.com/76438272.htm
正在保存阿朵拉的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫戴誉利，芳龄27，她在成都市
她的个人域名是://mm.taobao.com/516376911.htm
正在保存戴誉利的信息
未能获取到这个MM的个人域名和图片信息，请检查
正在查找第 3 页
发现一名模特，名字叫滕雨佳，芳龄24，她在杭州市
她的个人域名是://mm.taobao.com/539549300.htm
正在保存滕雨佳的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫张娟娟，芳龄27，她在广州市
她的个人域名是://mm.taobao.com/440678454.htm
正在保存张娟娟的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫沁源，芳龄26，她在杭州市
她的个人域名是://mm.taobao.com/73283141.htm
正在保存沁源的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫晓莉莉，芳龄26，她在广州市
她的个人域名是://mm.taobao.com/555178574.htm
正在保存晓莉莉的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫rikki，芳龄25，她在广州市
她的个人域名是://mm.taobao.com/290551947.htm
正在保存rikki的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫美高小咪，芳龄27，她在石家庄市
她的个人域名是://mm.taobao.com/689744369.htm
正在保存美高小咪的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫杨羽凡，芳龄24，她在杭州市
她的个人域名是://mm.taobao.com/745790526.htm
正在保存杨羽凡的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫未未，芳龄26，她在杭州市
她的个人域名是://mm.taobao.com/102188467.htm
正在保存未未的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫李柒柒，芳龄28，她在杭州市
她的个人域名是://mm.taobao.com/10378945.htm
正在保存李柒柒的信息
未能获取到这个MM的个人域名和图片信息，请检查
发现一名模特，名字叫倪佩婕，芳龄24，她在上海市
她的个人域名是://mm.taobao.com/93166849.htm
正在保存倪佩婕的信息
未能获取到这个MM的个人域名和图片信息，请检查
'''