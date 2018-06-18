import mmap

#创建一个24byte的二进制非空文件，b'\x00'并不是空byte字符串
size = 24
with open('demo.bin','wb') as wf:
	wf.seek(size-1)
	wf.write(b'\x00')
#将二进制文件映射到内存，r+b一般为固定值，二进制可读可写，会产生符合要求的fileno
with open('demo.bin','r+b') as f:
	fileno1 = f.fileno()
	#下面的代码必须放在with语句内，因为一旦文件关闭，文件描述符fileno1就失效了
	mm = mmap.mmap(fileno1,0,access=mmap.ACCESS_WRITE)
	print(mm[0])
	print(type(mm[0]))
	print(mm[:8])
	#切片赋值可以用byte字符串
	mm[0:8] = b'\x88'*8
	#必须用int来给单个元素赋值
	mm[0] = 100
