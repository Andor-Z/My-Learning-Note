Think Python
#C4.Case study: interface design

```
import sys
sys.path.append('C:\WinPython-64bit-3.4.3.4\swampy-2.1.5')

from TurtleWorld import *
TurtleWorld()
bob = Turtle()
fd(bob, 100)  #fd,bk 向前、向后
rt(bob)       #lt,rt 向左、向右
fd(bob, 100)  #pu,pd 笔抬起、笔放下
```


##4.3 Exercises
- 1、
```
def square(n):

	for i in range(4):
		fd(n, 100)
		rt(n)


import sys
sys.path.append('C:\WinPython-64bit-3.4.3.4\swampy-2.1.5')
from TurtleWorld import *
TurtleWorld()
bob = Turtle()
square(bob)
```
- 2.
```
def square(n, length):

	for i in range(4):
		fd(n, length)
		rt(n)


import sys
sys.path.append('C:\WinPython-64bit-3.4.3.4\swampy-2.1.5')
from TurtleWorld import *
TurtleWorld()
bob = Turtle()
square(bob, 200)
```

**encapsulation(封装)**
3、The functions lt and rt make 90-degree turns by default, but you can provide a second
argument that specifies the number of degrees.

```
def polygon(t, length= 200, n = 4):
	for i in range(n):
		fd(t, length)
		rt(t, 360/n)


import sys
sys.path.append('C:\WinPython-64bit-3.4.3.4\swampy-2.1.5')
from TurtleWorld import *
TurtleWorld()
bob = Turtle()
polygon(bob, 10, 50)
```
4.
```
import sys
sys.path.append('C:\WinPython-64bit-3.4.3.4\swampy-2.1.5')
from TurtleWorld import *
import math
def polygon(t, length, n ):
	for i in range(n):
		fd(t, length)
		rt(t, 360/n)
def circle(t, r):
	cicumference = 2 * math.pi * r
	n = int(cicumference / 3) +1
	length = cicumference / n
	polygon(t, length ,n )

TurtleWorld()
bob = Turtle()	
bob.delay = 0.01  #修改乌龟移动的速度
circle( bob, 60)
```
5.
```
import sys
sys.path.append('C:\WinPython-64bit-3.4.3.4\swampy-2.1.5')
from TurtleWorld import *
import math
def polygon(t, length, n ):
	for i in range(n):
		fd(t, length)
		rt(t, 360/n)
def arc(t, r, angle):
	cicumference = 2 * math.pi * r
	n = int(cicumference / 3) +1
	length = cicumference / n
	polygon(t, length ,n )

TurtleWorld()
bob = Turtle()	
bob.delay = 0.01  #修改乌龟移动的速度
circle( bob, 60)
```

#Chapter 5 Conditionals and recursion 条件和递归
##5.1 Modules operator 求与运算符'%'
##5.2 Bollean expressions 布尔表达式  ==  !=  >  <  >=   <=
##5.3 Logical operators 









