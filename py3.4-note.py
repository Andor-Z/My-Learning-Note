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




























