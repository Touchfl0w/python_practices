

#以文本方式打开文件，t默认；但如果要指明编解码方式，必须用关键字来指明参数，而不是位置参数
#rf为可迭代对象。每次迭代返回一行，返回值为字符串
with open('pingan.csv','rt',encoding='GB2312') as rf:
	text = rf.read()
	#文本模式下，读到的内容为str
	print(type(text))
	#看下只读+文本模式下，文件对象有哪些方法
	print(dir(rf))
	#查看文件对象有无写权限
	print(rf.writable())
	#返回当前文件指针的位置，单位byte;35689正好代表文件的大小
	print(rf.tell())
	#调整指针位置函数seek(offset,from_what=0)
	#定位到文件开始
	rf.seek(0)
	#查看当前指针位置
	print(rf.tell())
	#指针定位到文件尾
	rf.seek(0,2)
	#在文本文件中做如下随意定位指针的做法非常危险！不推荐
	rf.seek(10)
	print(rf.tell())
	#按行读取（\n)，返回结果为字符串
	rf.seek(0)
	print(rf.readline())
	#读取文件为列表，列表每个元素为文本中的一行，列表每个元素为字符串
	mylist = rf.readlines()
	print(mylist)













# with open('test1.csv','wt'encoding='utf-8') as wf:

# 	wf.write()












# #以二进制打开文本，要使用b;encoding仅用于文本模式
# with open('pingan.csv','rb') as rf:
# 	byte = rf.read()
# 	#读到的内容为byte,一种类字符串对象
# 	print(type(byte))
# 	print(byte)