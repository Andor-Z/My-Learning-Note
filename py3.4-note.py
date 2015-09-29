[TOC]
#Python基础
##数据类型和变量
`\`-------转义字符
`\n`-----换行
`\t`-----制表符
`r' '`----表示`''`内部的字符串默认不转义
`'''...'''`--三对引号表示多行内容
##空值`None`
**？**`//`---注释

`/`---除法结果浮点数
`//`--整除
##字符串 --格式化
`%`--格式化字符串
`%d`---整数
`%f`---浮点数
`%s`---字符串
`%x`---十六进制整数
eg:
```
>>>'Hi,%s, you have $%d.' %('Michael', 10000)
'Hi, Michael, you have $10000.'
```
当字符串里面的`%`是一个普通字符串，用`%`本身进行转义：`%%`

##列表list`[]` 元组tuple`()`
list.append(x)
	添加一个元素到列表的末尾，`a[len(a):] = [x]`
list.extend(L)
	将列表L中的所有元素附加到原列表list的末尾。`a[len(a):] = L`
list.insert(i, x)
	在给定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引
	所以 a.insert(0, x) 在列表的最前面插入，a.insert(len(a), x) 相当于 a.append(x)。
list.remove(X)
	删除列表中第一个值为X的元素，如果没有这样的元素将会报错。
list.pop([i])
	删除列表中给定位置的元素并返回它。如果未指定索引，a.pop()删除并返回列表中的最后一个元素。
	[]方括号表示这个参数是可选的
list.clear()
	删除列表中所有的元素。`del a[:]
list.index(x)
	返回列表中第一个值为x的元素的索引。如果没有这样的元素将会报错。
list.count(x)
	返回列表中x出现的额次数
list.sort(cmp=None, key=None, reverse=False)
	原地排序列表中的元素。
list.reverse()
	原地反转列表中的元素。
list.copy()
	返回列表的一个墙拷贝，等同于`a[:]`。


tuple
定义只有一个元素的tuple时，必须加一个,号消除歧义
`t = (45,)`

##条件判断

```
# -*- coding: utf-8 -*-
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#低于18.5：过轻
#18.5-25：正常
#28-32：肥胖
#高于32：严重肥胖
```
height = 1.75
weight = 80.5
bmi = weight/(heigtt**2)
if bmi< 18.5:
    pass
    #简单，未写完
```
##循环
```
# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']

for name in L:
	print('Hello, %s!' %(name))
```

##dict字典{}（dictionary）和set

###dict 中如果key不存在，dict就会报错
###dict的key必须是不可变对象

###set 一组不重复key的集合，但不存储value。
###要创建一个set，需要提供一个list作为输入集合
`s = set([1, 2, 3])
s
{1, 2, 3}
`

s.add(key) 添加元素到set
s.remove(key) 删除元素 

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交、并集

s1 & s2  #交际

s1 | s2 #并集

#函数
##调用函数
##定义函数

函数体内部的语句在执行时，一当执行到`return`时，函数就执行完毕，并将结果返回
如果没有`return`语句，函数执行完毕后也会返回结果，只是结果为`None`。
`return None`可以简写为`return`

**?**  `isinstance()`
**?**  `raise `
- 函数可以同时返回return多个值，也就是一个tuple

**练习**

请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax^2 + bx + c = 0的两个解。

提示：计算平方根可以调用math.sqrt()函数：
>>> import math
>>> math.sqrt(2)
1.4142135623730951



# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	delte = b**2 - 4*a*c
	if delte < 0:
		print("此一元二次方程无解。")
	elif delte == 0:
		ans = (-b)/(2*a)
		print("此一元二次方程有唯一解。唯一解为%f。" %ans)
	else:
		ans1 = (math.sqrt(delte) - b)/(2*a)
		ans2 = (-b - math.sqrt(delte))/(2*a)
		print("此一元二次方程有两个不同解，分别是%f和%f。" %(ans1, ans2))
# 测试:
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


##函数的参数
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n -1
		s = s * x
	return s

a = power(2,0)
b = power(2,45)
print(a)
print(b)

###可变参数

def calc(number):
	sum = 0
	for n in number:
		sum = sum + n *n
	return sum

calc([1,2,3]) #但是调用的时候，需要先组装一个list或 tuple
calc((1,2,3))


def calc(*number):
	sum = 0
	for n in number:
		sum = sum + n *n
	return sum

- 可变参数
*args  表示list
- 关键字参数
**   dict
- 命名关键字参数
* 分隔符

- 参数组合
def f1(a, b, c=0, *args, **kw):
	print('a=', a, 'b=', b,'c=', c,'args', args, 'kw', kw )

def f2(a, b, c = 0, *, d, **kw):
	print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=',kw)



f1(1, 2)

args = (1,2,3)
kw = {'d':99, 'x':'#', 'z':56,'fg':345}
f2(*args, **kw)

**?** dict的顺序


##递归函数

def fact(n):
	if n = 1:
		return 1
	return n * fact(n-1)

- 尾递归
在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num- 1, num* product)

- 练习


def move(n, a, b, c):
	if n == 1:
		print(a "--->" c)
	else:
		move(n-1, a, c, b)
		move(1, a, b, c)
		move(n - 1, b, a, c)



move(3, 'A', 'B', 'C')



#高级特性
##切片slice

##迭代iteration   for...in

d = {'a' : 1, 'b' : 2, 'c' : 3}

for i in d:
	print(i, end = ' ')

for i in d.values():
	print(i)

- 判断可迭代对象
- 通过collections 模块的Iterable

from collections import Iterable 
isinstance('abc', Iterable)

##列表生成式 List Comprehensions

L = []
for x in range(1, 11):
	L.append(x *x)

print(L)

[x * x for x in range(1, 11)]


- 两层循环

[m + n  for m in 'ABC' for n in 'abc']


- 三层的很少使用了

- 列出当前目录下的所有文件和目录名

import os
[d for d in os.listdir('.')]  #os.listdir可以列出文件和目录


d = {'x':'A' , 'Y': 'B', 'z': 'C'}
for k, v in d.items():
	print(k, ' ', v)

[k +'='+ v for k , v in d.items()]

l = ['Hello', 'World', 'IBN', 'Apple' ]

[a.lower() for a in l]

**练习**
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
AttributeError: 'int' object has no attribute 'lower'



L = ['Hello', 'World', 18, 'Apple', None]

[s.lower() for s in L if isinstance(s, str)]


##生成器
**生成器 generator**：一边循环一边计算

- 方法一
把列表生成式的[]改成()
L = [x *x for x in range(10)]
L

g = (x*x for x in range(10))
g




通过使用next()函数获得generator的下一个返回值



next(g)

g = (x*x for x in range(10))
for n in g:
	print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

 迭代器   

def triangle(n):
    L=[1]
    while True:
        yield(L)
        L.append(0)
        L=[L[i]+L[i-1] for i in range(len(L))]
        if len(L)>n:
            break/
    return "done"

g=triangle(15)
for i in g:
    print(i)

#函数式编程（Functional Programming）
纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

##高阶函数Higher-order function
###map/reduce

def add100(x):
	return x+100

hh = [11, 22, 33]

l = map(add100, hh)
list(l)
#输出[111, 122, 133]

2. 如果给出额外的可迭代参数，则对每个可迭代参数中的元素‘并行’

def abc(a, b, c):
	return a *10000 + b *100 + c

list1 = [11, 22, 33]
list2 = [44, 55, 66]
list3 = [77, 88, 99]

list(map(abc, list1, list2, list3))

#输出[114477, 225588, 336699]


reduce: 把一个函数作用在一个序列[x1, x2, x3......]上,这个函数必须接收2个参数
reduce(f, [x1,  x2, x3]) = f(f(f(x1, x2),x3),x4)

from functools import reduce
def add(x, y):
	return x+y

reduce(add, [1, 3,4,5,7])

from functools import reduce
def fn(x, y):
	return x*10 +y

def char2num(s):
	return{}



def normalize(name):


###7.1.2 map/reduce