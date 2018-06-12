#文本附加模式：在源文件末添加文本
#说明write.txt初始文本为：xxxxxxxxxx
with open('write.txt','at',encoding='utf-8') as f:
	print(f.readable())
	print(f.writable())
	f.write('cacacac')

with open('write.txt','r',encoding='utf-8') as rf:
	print(rf.read())

#文本读写w+t:该模式下写会将源文件内容擦掉并写入新内容
with open('write.txt','w+t',encoding='utf-8') as f:
	#指针位于文件首
	print(f.tell())
	#原始内容被擦掉，所以内容为空
	print(f.read())
	f.write('xxxxxxxxxx')
	f.seek(0)
	print(f.read())

#文本读写a+t:该模式下初始指针位于文件尾，读写均要注意指针位置
with open('write.txt','a+t',encoding='utf-8') as f:
	f.write('aaa')
	#指针位于文件尾，读取为空
	print(f.read())
	f.seek(0)
	print(f.read())

#文本读写r+t:初始指针位于文件头，源文件内容未擦除，进行覆盖写；读的话严格按照指针位置进行读
with open('write.txt','r+t',encoding='utf-8') as f:
	f.write('AAAAAAAA')
	print(f.tell())
	print(f.read())
	
