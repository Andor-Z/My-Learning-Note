import feedparser
import re

# http://feed.cnblogs.com/blog/u/161528/rss
def getwordcounts(url):
    '''
    Return title and dictionary of word counts for an RSS feed 
    返回一个RSS订阅源的标题和包含单词计数情况的字典
    '''
    d = feedparser.parse(url)
    #print(d.entries)
    wc = {}

    # Loop over all the entries
    # 循环遍历所有的文章条目
    for e in d.entries:
        # print(e)
        # print(e.summary)
        # print('******\n')
        # print(e.description)
        if 'summary' in e:
            summary = e.summary
            #print(summary)
        else:
            summary = e.description

        # Extract a list of words
        # 提取一个单词列表
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            # 若 word 在wc中则返回对应的值，若键不在则向字典插入word，并返回0
            wc[word] += 1
    return d.feed.title, wc
            

def getwords(html):
    # Remove all the HTML tags
    # 将html中的pattern替换为空格
    txt = re.compile(r'<[^>]+>').sub('',html)

    # Split words by all non-alpha characters
    # 通过所有的非字母符拆分出单词
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    # 转化成小写形式
    return [word.lower for word in words if word != '']

apcount ={}
wordcounts = {}
feedlist = [line for line in file(r'chapter3\feedlist.txt')]
 for feedurl in feedlist:
    try:
        title, wc = getwordcounts(feedurl)
        wordcounts[title] = wc 
        for word,count in wc.items():
            apcount.setdefault(word, 0)
            if count>1:
                apcount[word]+=1
    except:
        print('Failed to parse feed %s' %feedurl)

wordlist=[]
for w,bc in apcount.items():
    frac=float(bc)/len(feedlist)
    if frac>0.1 and frac<0.5:
        wordlist.append(w)




    