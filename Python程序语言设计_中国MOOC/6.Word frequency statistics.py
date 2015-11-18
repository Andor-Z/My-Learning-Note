#6.Word frequency statistics.py

def main():
	filename = input('enter a filename:').strip()
	infile = open(filename,'r')

	#建立用于计算词频的空字典
	wordcounts = {}
	for line in infile:
		processLine(line.lower(), wordcounts)
