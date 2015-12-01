import os
path = input('输入一个路径：')
for root, dirs, files in os.walk(path):
	for name in files:
		print(root)
		print(name)
		print(os.path.join(root,name))