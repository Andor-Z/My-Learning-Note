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

##dict字典（dictionary）和set




