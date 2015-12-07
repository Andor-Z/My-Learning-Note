#1.2 Unpacking Elements from Iterables of Arbitrary Length
#解压可迭代对象赋值给多个变量
##star unpacking

def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)

#the middle variable will always be a list 

#星号表达式在迭代元素为可变长元组的序列时

recods = [
	('foo', 1, 2),
	('bar', 'hello'),
	('foo', 3, 4)
]

def do_foo(x, y):
	print('foo', x, y)

def do_bar(s):
	print("bar", s)

for tag, *args in recods:
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)


#star unpacking 在字符串的分割上

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(fields)

#递归算法
items = [1, 10, 7, 4, 5, 9]

def sum(items):
	head, *tail = items
	return head +sum(tail) if tail else head #python 中的三元表达式


print(sum(items))