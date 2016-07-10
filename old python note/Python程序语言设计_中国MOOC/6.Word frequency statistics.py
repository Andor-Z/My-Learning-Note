#6.Word frequency statistics.py
import turtle
##全局变量##
#词频排列显示个数
count = 10
#单词频数数组-作为y轴
data = []
#单词数组- 作为x轴
words = []

###############   Turtle Start   #########################
##!!!未绘制


#对文本的每一行计算词频
def processLine(line, wordcounts):
	#空格替换标点符号
	line = replacePunctuations(line)
	words = line.split()
	for word in words:
		if word in wordcounts:
			wordcounts[word] += 1
		else:
			wordcounts[word] = 1

#空格替换标点符号的函数
def replacePunctuations(line):
	for ch in line:
		if ch in r'~@#$%^&*()_-+=<>?/,.:;{}[]|\'"':
			line = line.replace(ch, ' ')
	return line

def main():
	filename = input('enter a filename:').strip()
	infile = open(filename,'r')

	#建立用于计算词频的空字典
	wordcounts = {}
	for line in infile:
		processLine(line.lower(), wordcounts)

	#从字典中获取数据对
	pairs = list(wordcounts.items())
	#对列表中的数据进行对换位置，并排序
	items = [[x, y] for (y, x) in pairs]
	items.sort()

	#输出count个词频结果
	for i in range(len(items)-1,len(items)-count -1, -1 ):
		print(items[i][1]+'\t'  +str(items[i][0]))
		data.append(items[i][0])
		words.append(items[i][1])

	infile.close()



if __name__ == '__main__':
	main()