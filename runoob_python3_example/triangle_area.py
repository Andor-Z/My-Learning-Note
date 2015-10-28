#triangle area
#已知三角形三边长，求三角形面积

def t_area(a, b, c):
	#计算半周长
	p = (a + b +c) / 2

	#利用海伦公式计算面积

	area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
	return area 
