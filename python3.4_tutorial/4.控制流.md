# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:10:45 2015

@author: ZYF
"""
# 4.1 if语句


#x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


#4.2 for 语句

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
     
for w in words[:]:   #Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
words 


# 4.3 range() 函数

for i in range(5):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# 4.4 break  continue
# break用于跳出最近的for或while循环

for n in range(2, 10):
    for x in range(2, n):
        if n % x ==0:
            print(n, 'equals', x, '*', n//x)
            break  
#此处使用break是表示当n可以由一组数相乘可以得到后，无需再寻找其他的数相乘了
    else:
        #loop fell through without finding a factor
        print(n, 'is a prime number')

  
  
# continue 表示继续下一次迭代

for num in range(2,10):
    if num % 2 == 0:
        