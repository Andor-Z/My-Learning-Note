import re

str1 = 'imooc python'

#print(imooc.read())
def regul_ex1(fname, s):
	imooc = open(fname)
	imooc_p = re.compile(s)
	imooc_r = imooc_p.match(imooc.read())
	#print(imooc_r)

f = 'imooc.txt'
s = 'imooc'
#regul_ex1(f,s)

def regul_ex2():
	pa = re.compile(r'imooc')
	ma = pa.match(str1)
	print(ma.group())

regul_ex2()

