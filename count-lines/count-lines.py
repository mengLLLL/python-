
def count_lines():
	print(files)
	line_sum,blank,note=0,0,0
	f = open('./test.txt','r')
	lines = f.readlines()
	print (lines)
	length = len(lines)
	print (length)
	#遍历每个文件的每行来看是代码还是\n还是注释
	for line in lines:
		print (line)
		if line.startswith('#'):
			#startswith不是startwith，太他妈坑了！
			note += 1
		elif line == '\n':
			blank +=1
	print (length,blank,note)


if __name__ == '__main__':
	count_lines()