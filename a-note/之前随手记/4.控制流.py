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
        print('Found a even number', num)
        continue
    print('Found a number', num)


# 4.5 pass语句
##创建最小的类

class MyEmptyClass:
    pass


# 4.6 定义函数
## 创建一个生成任意上界斐波那契（Fibonacci）数列的函数
def fib(n):   #write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1 
    while a < n:
        print(a, end=' ')   #为何使用end后，所有的print在同一行
        a, b = b, a+b
    print()  #?这句print的用处


#### （n）为形式参数  （）中为形式参数列表
####函数体的第一行可以是一个可选的字符串文本；此字符串是该函数的文档字符串，或称为docstring。
####有工具使用 docstrings 自动生成在线的或可打印的文档，或者让用户在代码中交互浏览；
####在您编写的代码中包含 docstrings 是很好的做法，所以让它成为习惯吧。
####变量引用首先查找局部符号表，然后是上层函数的局部符号表，然后是全局符号表，最后是内置名字表。


###返回斐波那契数列列表的函数，不是打印出来的
def fib2(n): #return Fibonacci series up to n 
    """Return a list containing the Fibonacci series up to n,"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  #see below
        a, b = b, a+b
    return result

f100 = fib2(100)  #call it 
print(f100)               #write the result

####append() 方法是list 对象定义的。它在列表的末尾添加一个新的元素。在本例中它等同于result = result +[a]，但效率更高。




