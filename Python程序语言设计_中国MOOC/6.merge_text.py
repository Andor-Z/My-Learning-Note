#6.merge_text.py
#合并信息

def main():
	ftele1 = open('6.TeleAddressBook.txt','rb') #以二进制打开，保证编码正确
	ftele2 = open('6.EmailAddressBook.txt', 'rb')

	ftele2.readline()#跳过第一行
	ftele1.readline()
	line1 = ftele1.readlines()
	line2 = ftele2.readlines()

	list1_name = []
	list1_tele = []
	list2_name = []
	list2_email = []

	for line in line1:
		elements = line.split()
		list1_name.append(str(elements[0].decode('gbk')))
		list1_tele.append(str(elements[1].decode('gbk')))
		#将文本读出来的bytes转换为str

	for line in line2:
		elements = line.split()
		list2_name.append(str(elements[0].decode('gbk')))
		list2_email.append(str(elements[1].decode('gbk')))

	lines = []
	lines.append('姓名\t 电话\t 邮箱\n')

	#遍历姓名列表1
	for i in range(len(list1_name)):
		s = ''
		if list1_name[i] in list2_name:
			j = list2_name.index(list1_name[i])
			s = '\t'.join([list1_name[i],list1_tele[i], list2_email[j], '\n'])
			#s += '\n'
		else:
			s = '\t'.join([list1_name[i],list1_tele[i], str('-----'), '\n'])
			#s += '\n'
		lines.append(s)

	#处理列表2
	for i in range(len(list2_name)):
		s = ''
		if list2_name[i] not in list1_name:
			s = '\t'.join([list2_name[i],str('-----'), list2_email[i], '\n'])
		lines.append(s)

	#print(lines)

	ftele3 = open('AddressBook.txt', 'w')
	ftele3.writelines(lines)
	ftele1.close()
	ftele2.close()
	ftele3.close()



if __name__ == '__main__':
	main()




