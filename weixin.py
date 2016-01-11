import xlrd
import os

def find_all_file(file_dir):
	for root,dirs,files in os.walk(file_dir):
		if 'all_files.txt' in files:
			f = open('all_files.txt','r+')
			lines = f.readlines()
			for i in files:
				exc_n = i + '\n'
				if exc_n in lines:
					files.remove(i)
				else:
					f.tell()
					f.write(exc_n)
					f.close()

			return files
		else:
			f = open('all_files.txt','w')
			
			f.close()
			return files


b = 'C:\\workspace\\test'
a = find_all_file(b)
print(a)
