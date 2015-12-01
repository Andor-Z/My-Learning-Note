import turtle
import math
bob = turtle.Turtle()
bob.shape('turtle')
#bob.speed(6)  可以设置速度
#'fastest' :  0     'fast'    :  10       'normal'  :  6   'slow'    :  3 'slowest' :  1

#fd(forward) bk 向前 向后
#lt rt 向左 向右
#pu pd 抬笔 放笔

def square(length=150):
	for i in range(4):
		bob.fd(length)
		bob.lt(90)



def polygon(length= 100, silde = 4):
	
	for i in range(silde):
		bob.fd(length)
		degree = 360/silde
		bob.lt(degree)

#polygon(silde = 6)


def circle(radius=50 , silde = 50 ,spee = 6):  #radius 半径
	bob.speed(spee)
	for i in range(silde):
		
		bob.fd(2*math.pi*radius/silde)
		degree = 360/silde
		bob.left(degree)


#circle(radius = 100, silde = 100, spee = 1)
#circle(radius = 120, silde = 100, spee = 0)


def arc(radius=50, angle = 360, spee = 6,silde = 100):
	'''
自定义画多大部分的圆
radius  半径
angle  角度，即画圆的多大部分
spee 速度  'fastest':0 'fast':10 'normal':6 'slow' :3 'slowest' :  1
silde 即画多少边，此圆并非真正的圆，而是多边形，边数越多，越接近圆
	'''
	bob.speed(spee)
	silde1=int(angle/360*silde)
	for i in range(silde1):
		
		bob.fd(2*math.pi*radius/silde)
		degree = 360/silde
		bob.left(degree)

arc(angle = 250)







#world = TurtleWorld()

#print(bob)





