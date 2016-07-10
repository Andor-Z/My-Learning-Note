[toc]
learn python the hard way
http://learnpythonthehardway.org/book/
http://www.swaroopch.com/notes/python/
http://itlab.idcquan.com/linux/manual/python_chinese/index.html


# --coding: utf-8 --
#第一行加入此代码，表示使用utf-8编码

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

ex11

print("How old are you?", end= '')
age = input()
print("How tall are you?", end = ' ')
height = input()

print(('So, you\'re %s old, %r tall.') %(age, height))
#print('So, you\'re %s old, %r tall.' %(age, height))
#使用%r时输出时会带有''号，而使用%s时则不会出现



ex13

from sys import argv

script, first, second, third = argv

print('The script is called:', script)
print(first)
print(second)
print(third)


ex14

from sys import argv
script, user_name = argv
prompt = '>  '

print("Hi %s, I'am the %s script." %(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me, %s?" %user_name )
likes = input(prompt)

print("Where do you live %s?" %user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer= input(prompt)

print('''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' %(likes, lives, computer))



ex15

from sys import argv
script, filename = argv

txt = open(filename)

print("Here's your file %r:" %filename)
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()


ex16
close---关闭文件
read----读取文件内容，可以把结果赋给一个变量
readline-读取文本文件中的一行
readlines-读取文件全部内容，分行以列表形式存储
truncate-清空文件
write(stuff) - 将stuff写入文件

from sys import argv

scipt, filename = argv
print("We're going to erase %r." % filename)

print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Operning the file...")
target = open(filename, 'w')

print("Truncating the file. Godbye!")

target.truncate()


print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")


target.write("%s\n%s\n%s" %(line1, line2, line3))

target.close()

t = open(filename)
print(t.read())
t.close()

ex17

from sys import argv
from os.path import exists
#os.path exists文件或者目录是否存在，bool值

script, from_file, to_file = argv
print("Copying from %s to %s" %(from_file, to_file))

#we could do these two on one line too , how?
input = open(from_file)
indata = input.read()

print("The input file is %d bytes long." %len(indata))

print("Does the output file exist? %r" %exists(to_file))
print('Ready, hit RETURN to continue, CTRL-C to abort.')
# ? input() 可能由于input已经被定义了

output = open(to_file, 'w')
output.write(indata)

print('Alright, all done.')

output.close()
input.close()



#确实是由于input已经被使用
from sys import argv
from os.path import exists
#os.path exists文件或者目录是否存在，bool值

script, from_file, to_file = argv
print("Copying from %s to %s" %(from_file, to_file))

#we could do these two on one line too , how?
input1 = open(from_file)
indata = input1.read()

print("The input file is %d bytes long." %len(indata))

print("Does the output file exist? %r" %exists(to_file))
print('Ready, hit RETURN to continue, CTRL-C to abort.')
input()

output = open(to_file, 'w')
output.write(indata)

print('Alright, all done.')

output.close()
input1.close()


ex18

def print_two(*args):
	arg1, arg2 = args
	print('arg1: %r, arg2: %r' % (arg1, arg2))

print_two('zhao', 'yu')
print_two('zhao', 'yu','fei')


ex19


from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	for i in range(1,line_count+1):
		print(i, f.readline())

current_file = open(input_file)

print('First let\'s print the whole file:\n')

print_all(current_file)

print('Now let\'s rewind, kind of like a tape')

rewind(current_file)

print('Let\'s print three lines:')

current_line = 3
print_a_line(current_line, current_file)


ex21

def add(a, b):
	print('ADDING %d + %d' %(a, b))
	return a + b

def subtract(a, b):
	print('SUBTRACTING %d + %d' %(a, b))
	return a - b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)


ex24

print("Let's practice everything.")

print('You\'d need to know \'bout escapes with \\that do \n newlines and \t tabs.')

poem = """
\t The lovely world 
with logic so firmly planted
cannot discern passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print('----------')
print(poem)
print('----------')

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)


ex27 boolean logic expression













