[TOC]
tags: head_first python 
#1 初识python
##人人都爱列表

movies = ['The Holy Grail', 'The Life of Brian', 'The Meaning of Life']
print(movies[1])

## An IDLE Session IDEL会话

cast = ['Cleese', 'Palin', 'Jones', 'Idle']
print(len(cast))

### append() 在列表末尾增加一个数据项
cast.append('Gilliam')


###pop()从列表末尾删除数据
cast.pop()
print(cast)

###extend() 在列表末尾增加一个数据项集合

cast.extend(['Gilliam', 'Chapman']


###remove() 在列表中找到并删除一个特定的数据项

cast.remove('Chapman')

### insert() 在某个特定的位置前面增加一个数据项
cast.insert(0, 'Chapman')


###迭代
fav_movies = ['The Holy Grail', 'The Life of Brian']
for each_flick in fav_movies:
	print(each_flick)
	
>  “组”(suite)：冒号后面的代码
>   目标字符： target identifier

fav_movies = ['The Holy Grail', 'The Life of Brian']
count = 0 
while count < len(fav_movies):
	print(fav_movies[count])
	count = count + 1
```python
###列表嵌套
movies = ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam']]]
print(movies[4][1][2])

for each_item in movies:
	print(each_item)
```
> **BIF**：built-in function 内建的函数

> **`isinstance()`**: 允许检查某个特定标识符是否包含某个特定类型的数据

```
name = ['m', 't']  
isinstance(name, list)

for each_item in movies:
	if isinstance(each_item,list):
		pass
	else:
		print(each_item)


def lol(the_list):
	'''注释函数'''
	for each_item in the_list:
		if isinstance(each_item, list):
			lol(each_item)
		else:
			print(each_item)

```


##Python工具箱
###术语
> "**BIF**":内置函数
> "组（suite）": 代码块，通过缩进来指示分组
>"功能齐全（Batteries included）": Python提供了快速高效的完成工作所需的大多数功能

# 2 共享你的代码——函数模块
- **模块和一些发布工具**
	- 模块允许你合理组织代码来实现最优共享
	- 发布工具允许你向全世界共享你的模块
	
 

- 三重引号来建立多行注释

- 计算机上的Python模块
```
import sys
sys.path
```

## distribution(发布)
###1、创建一个文件夹，把将要发布的test.py模块文件复制到这个文件夹中
###2、在新文件夹中创建一个名为“stetuo.py”的文件

```python
from distutils.core import setup

setup(
	name       = 'test',
	version    = '1.0.0',
	py_modules = ['test'],
	author = 'Andor-z',
	urld = 0,
	description = 'A python code distribution test',

	)
```
###3、构建发布
windows环境下
```
C:\Python34\python.exe setup.py sdist  #构建一个发布文件
```
```
C:\Python34\python.exe setup.py install   #将发布安装到python的本地副本中
```
###4、导入模块并使用
一
```
import test
test.lol()
```
二 
```
from test import lol
lol()
```
- BIF内置函数
`list()` 创建一个新的空列表
`range()`返回一个迭代器，根据需要生成一个指定范围内的数字
`enumerate()`创建成对数据的一个编号列表，从0开始
`int()`
`id()`返回一个python数据对象的唯一标识
`next()`返回一个可迭代数据结构中的下一项
- 包含`end =''`作为`print()`BIF的一个参数会关闭其默认行为（即在输入中自动包含换行）

- API(Application Programming Interface):应用程序编程接口

```
def lol(the_list,level = 0):
	'''注释函数'''
	for each_item in the_list:
		if isinstance(each_item, list):
			lol(each_item, level = level +1) 
		else:
			for each_level in range(level):
				print('\t', end= '') #\t  TAB
			print(each_item)

```

#3、文件与异常
```
the_file = open('sketch.txt')
the_file.close
```

## An IDLE Session  idel会话
```
import os #从标准库导入os
os.getcwd() #当前工作的目录
os.chdir('/hfpython/chapter3') #切换工作目录为包含数据文件的文件夹，注意'\','/'

data = open('sketch.txt') 
print(data.readline(), end ='')
#退回到文件起始位置，使用for语句处理文中每一行
data.seek(0)  #对于python文件也可以使用'tell()'
for each_line in data:
	print(each_line, end = '') #????为何此处输出行，而不是每一个单词
```
- `split()`分割数据
```
data = open('sketch.txt')
for each_line in data:
	(role, line_spoken) = each_line.split(':')
	print(role,end= '')
	print(' said:', end= '')
	print(line_spoken, end = '')
```
当一行中出现多个':'时，代码会提示错误`ValueError`
- 为了解决这个问题，我们可以使用`help()`BIF
```
>>>help(each_line.split)
Help on built-in function split:

split(...) method of builtins.str instance
    S.split(sep=None, maxsplit=-1) -> list of strings

    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.

```
`maxslit`这个参数控制着将数据分阶为多少个部分。默认值时数据会尽可能的分解。当将这个值设置为1时，数据只会分解成两部分

```
data = open('sketch.txt')
for each_line in data:
	(role, line_spoken) = each_line.split(':', 1)
	print(role,end= '')
	print(' said:', end= '')
	print(line_spoken, end = '')
```

* 出现缺少':'的情况
- 出现大量意外情况的处理办法
	1、增加额外的逻辑来进行处理。如果有更多担心的问题就需要更多的代码
	2、允许这些错误的发生，然后在各个错误确实发生时分别处理相应的错误

```
data = open('sketch.txt')
for each_line in data:
	if each_line.find(':') != -1: # if not each_line.find(':') == -1 :
		(role, line_spoken) = each_line.split(':', 1)
		print(role,end= '')
		print(' said:', end= '')
		print(line_spoken, end = '')
	else:
		print(each_line, end = '')

data.close()
```
## 处理异常（exception）
###`try`/`except`机制
使用`try`保护代码，使用`except: pass`忽略可能出现的错
```
data = open('sketch.txt')
for each_line in data:
	try:
		(role, line_spoken) = each_line.split(':', 1)
		print(role,end= '')
		print(' said:', end= '')
		print(line_spoken, end = '')
	except:
		pass

data.close()
```

```
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			print(role,end= '')
			print(' said:', end= '')
			print(line_spoken, end = '')
		except ValueError:
			pass

	data.close()
except IOError:
	print('The data file is missing!')
```

#第四章 持久化：将数据存成文件 
 
>	 
　　3. 不管try/except语句中是否有异常发生，finally的代码段总是会被执行； 
　　4. 异常对象会传入到except代码段，并且可以使用as关键字将其赋值给一个标识符； 
　　5. str()内置函数可以用来访问任何数据对象的字符串表示，前提是该数据对象支持该转换； 
　　6. locals()内置函数返回当前作用范围内的变量集合； 
　　7. in操作符可用于测试成员包含关系； 
　　8. "+"操作符应用于两个字符串时会得到它们的串联结果，而应用于数字时会得到它们的相加和； 
　　9. with语句即使在异常发生的情况下，也会自动去关闭所有打开的文件。with语句同样可以使用as关键字； 
　　10. sys.stdout是Python中的标准输出，它位于标准库中的sys模块； 
　　11. 标准库pickle模块可以让轻松高效地保存Python数据对象到磁盘和从磁盘恢复Python数据对象； 
　　12. pickle.dump()函数将数据存盘； 
　　13. pickle.load()函数从磁盘恢复数据。
关于笔记的排版与构架：因为自己不能很好的把握一章的结构，所以从本章开始尝试完全使用书中结构
##1. `strip()`方法移除字符串首尾空白字符； 程序生成数据
```
man = []
other = []
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()  #strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass

	data.close()
except IOError:
	print('The data file is missing!')
print(man)
print(other)
```

##2. print()内置函数中的file参数可以控制data是读入或是写出；以写模式打开文件
`open()`默认模式r表示读
`out = open('data.out', 'w')` 'w'模式表示写
###`open()`模式
1、追加到一个文件使用'a'模式
2、如果一个文件已经存在，使用'w'模式会清空它现有的内容
 -  默认`print()`显示数据时会使用标准输出：屏幕，要把数据写至一个，需要使用file参数
`print('hello, world', file = out)`
 -  一定要关闭文件，确保所有数据都写入磁盘。刷新输出（flushing）
`out.close()`


```
man = []
other = []
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()  #strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass

	data.close()
except IOError:
	print('The data file is missing!')
try:
	man_file = open('man_data.txt','w')  # 必须将打开的文件赋值到一个变量
	other_file = open('other_data.txt', 'w')
	print(man, file = man_file)
	print(other, file = other_file)
	man_file.close()
	other_file.close()
except:
	print('A error!')

```
##3. 不管try/except语句中是否有异常发生，finally的代码段总是会被执行；

```
man = []
other = []
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()  #strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass

	data.close()
except IOError:
	print('The data file is missing!')
try:
	man_file = open('man_data.txt','w')  # 必须将打开的文件赋值到一个变量
	other_file = open('other_data.txt', 'w')
	print(man, file = man_file)
	print(other, file = other_file)
	man_file.close()
	other_file.close()
except:
	print('A error!')
finally:
	man_file.close()
	other_file.close()

```






