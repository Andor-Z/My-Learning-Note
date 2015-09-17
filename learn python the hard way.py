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
p63

















