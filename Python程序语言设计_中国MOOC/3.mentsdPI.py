#通过蒙特卡诺方法求Pi值
from random import random
from math import sqrt
from time import clock

darts = 2**20
hits = 0
clock()
for i in range(1, darts):
	x, y = random(), random()
	dist = sqrt(x**2 + y**2)
	if dist <= 1.0:
		hits = hits +1
pi = 4*(hits/darts)

print("Pi的值是%s" % pi)
print("程序的运行时间是%-5.5ss" %clock())
