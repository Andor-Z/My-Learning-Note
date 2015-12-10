def find_start_imooc(fname):
	f = open(fname)
	for line in f:
		if line.startswith('imooc'):
			print(line)

#find_start_imooc('imooc.txt')

def find_in_imooc(fname):
	f = open(fname)
	for line in f:
		if line.startswith('imooc') and line[:-1].endswith('imooc'):
			print(line)




#find_in_imooc('imooc.txt')


# 匹配一个下划线和字母开头的变量名

a = '_value'
#print(a and (a[0]== '_' or 'a' <= a[0] <= 'Z'))



