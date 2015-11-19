#6.Word frequency statistics.py

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
