[TOC]  
廖雪峰Python3教程--函数式编程  
#7.函数式编程（Functional Programming）
纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。

##7.1高阶函数Higher-order function  
###7.1.1 map/reduce  
###7.1.2 filter
'filter()'接收一个函数和一个序列，把传入的函数依次作用于每个元素，然后根据返回值是'True'还是'False'决定去流。

###7.1.3 sorted
高阶函数
关键字`key`  `reverse = True False`

##7.2 返回函数
闭包 嵌套了函数，暂时用不到这么高级的内容，有部分不太理解

一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

#7.3 匿名函数 `lambda`

计算 `f(x) = x^2` 

匿名函数
`list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))`

`lambda x: x*x` 实际上是
```
def f(x):
	return x *x
```

a = [x*x for x in range(1,10)]
print(a)

- 函数式编程中很多高阶函数只是一带而过

#8 模块

##8.1 使用模块

`__name__` 
当我们在命令行运行Py文件时，python解释器把一个特殊变量`__name__`置为`__main__`

- 作用域 
python中通过前缀`_`实现作用域
可以直接引用的 public 公开变量 

`__xxx__`特殊变量，可以被直接引用，但是一般是有特殊用途，如 __author__        __name__  __doc__

`_xxx` `__xxx`非公开函数private 不应该被直接引用， 但是可以引用，从编程习惯上不应该引用private函数或者变量

##8.2 安装第三方模块


#9 面向对象编程

`object oriented programming `

##9.1 类和实例

类 class 实例的模板，
实例 instance  一个个具体的对象
方法 就是与实例绑定的函数，方法可以直接访问实例的数据

```
class Student(object): #类名称开头字母通常大写

	def __init__(self, name, score): # __init__ 方法的第一个参数永远是self,表示实例本身
	# name, score 都是 类的属性
		self.name = name
		self.score = score

	def print_score(self):
		print('%s:%s' %(self.name, self.score))


bart = Student('Bart Simpson', 59)

bart.print_score()
```

##9.2 访问限制

如果要让内部属性不被外部访问，可以把属性的名称前加两个下划线__,变成私有变量private，只有内部可以访问，外部不能访问

```
class student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s:%s' %(self.__name, self.__score))
```

如果外部代码需要获取name score 属性，需要给Student类增加 方法

##9.3 继承和多态

##9.4 获取对象信息

type()

isinstance()

dir()

```
hasattr(obj, 'x') # 有属性'x'吗？

hasattr(obj, 'y') # 有属性'y'吗？

setattr(obj, 'y', 19) # 设置一个属性'y'

getattr(obj, 'y') # 获取属性'y'

```


##9.5 实例属性与类属性


#10 面向对象高级编程

多重继承  定制类 元类

##10.1 使用__slots__

限制实例的属性
···
class Student():
	__slots__ = ('name', 'age')
```
对继承的子类并不起作用

##10.2 使用 @property

python 内置装饰器 @property  

```
class Screen(object):
	def __init__(self, width, height):
		self._width = width
		self._height = height 


	#__slots__ = ('width', 'height', 'resolution') 由于有变量冲突不可以用，不知道为啥


	@property
	def width(self):
	    return self._width

	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise ValueError('width must be an integer.')
		self._width = value

	@property
	def height(self):
	    return self._height

	@height.setter
	def height(self, value):
		if not isinstance(value, int):
			raise ValueError('height must be an integer.')
		self._height = value
	
	@property
	def resolution(self):
	    return self._height *self._width
	


s = Screen(1024,768)
#s.width = 1024
#s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
```

##10.3 多重继承

MixIn

##10.4 定制类

- `__str__`

- `__iter__` `__next__`

- `__getitem__`

- `__getattr__`

- `__call__`

不懂的地方好多！！！！



##10.5 使用枚举类


##10.6 使用元类




#11 错误、调试和测试

##11.1 错误处理
```
try:

except       as e:


finally:

```

- 调用堆栈

这一章很蛋疼

#12 IO编程

stream 流
同步IO

异步IO
	回调模式
	轮询模式
	
##12.1 文件读写

```
try:
	f = open(r'D:\GitHub\Python-note\test.txt')
	a = f.read()
	print(a)
finally:
	f.close()
```
```
with open(r'D:\GitHub\Python-note\test.txt', 'r') as f:
	print(f.read())
```

read(size)方法

readline()
readlines()  一次读取所有内容并按行返回list


 字符编码
open(r"", encoding = 'gbk')

当遇到有些编码不规范的的文件，你可能会遇到`UnicodeDecodeError`,因为在文本文件中可能夹杂了一些非法编码的字符。解决办法是
f = open(r'', encoding = 'gbk', errors = 'ignore')

写文本文件 `'w'`  写二进制文件`'wb'`

##12.2 StringIO BytesIO

StringIO
```
from io import StringIO
f = StringIO()
print(f.write(u'hello'))
print(f.getvalue())
```

BytesIO

```
from io import BytesIO
f = BytesIO()
f.write('中文',encode('utf-8'))  #这段代码运行有问题
```

这节不懂。。。。。


##12.3 操作文件和目录

```
import os
print(os.name)
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
#print(os.uname())
#uname()函数在Windows上不提供
os.environ

#获取某个环境变量的值
os.environ.get('PATH')

```
import os
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')

# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')
#路径拆分
os.path.split()
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
#路径合并
os.path.join()
#文件扩展名
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')

# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')


#shutil模块  os模块的补充
```

#当前目录下所有目录
import os
[x for x in os.listdir('.') if os.path.isdir(x)]

os.listdir 当前目录下所有内容
os.path.isdir 某一路径是否为目录


#列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

- Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。


##12.4 序列化

把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等


#13 进程和线程



#14 正则表达式

'\d' 匹配一个数字
'\w' 匹配



























