# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 12:39:47 2014

@author: Zilongfei
"""
a = 'ABC'
b = a
a = 'XYZ'
#\n 表示换行
#\t 表示一个制表符
#\\ 表示 \ 字符本身

print b
print u'中文'
print u'中文\n日文\n韩文'
print u'''中文
日文
韩文'''
# -*- coding: utf-8 -*-
#上行解释目的是告诉Python解释器，用UTF-8编码读取源代码。
print u'''静夜思

床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''

#整数和浮点数
num=49
#//取整
tens=num//10
#%取余
ones=num%10
print tens,ones
print tens*10 + ones

#Python把0、空字符串''和None看成 False，
#其他数值和非空字符串都看成 True
a = True
print a and 'a=T' or 'a=F'
#4.1创建list
L = [95.5,85,59]
print L[0]
print L[1]
print L[2]
print L[-1]
print L[-2]
print L[-3]
L = ['Adam', 'Lisa', 'Bart']
#append()总是把新的元素添加到 list 的尾部。
L.append('Paul')
print L
L = ['Adam', 'Lisa', 'Bart']
L.insert(0, 'Paul')
print L
#pop()方法总是删掉list的最后一个元素，并且它还返回这个元素
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
L.pop(2)
print L
#tuple和创建list唯一不同之处是用( )替代了[ ]。
#tuple一旦创建完毕，就不能修改了。
t = (0,1,2,3,4,5,6,7,8,9)
print t
t = ()
print t
t =(1)
print t
t= (1,)
print t
t = ('a', 'b', ['A', 'B'])

#if 语句
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
print 'END'
#if ... 多个elif ... else ... 
#for
L = ['Adam', 'Lisa', 'Bart']
for A in L:
    print A

sum = 0
x = 1
while x < 100:
    sum = sum + x
    x = x +2
print sum

L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name
    
sum = 0
x = 1
n = 1
while True:
    sun = sum + x
    x = x * 2
    n = n + 1
    if n > 20:
        break
print sum

sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x
print sum

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print x*10+y
        
for x in [ 1,2,3,4,5,6,7,8,9 ]:
    for y in [0,1,2,3,4,5,6,7,8,9 ]:
        if x < y:
            print x*10+y    
            
#dict
d = {'Adam' : 95,'Bart': 85,'Lisa': 59} 
print d['Adam']  
print d.get('Adam')         
        
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for n in d:
    print n ,':',d[n]       
        
        
        
        
        
        
        
        


