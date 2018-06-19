import os 

#调用系统stat函数,对于link文件，针对其源文件调用函数
s = os.stat('demo.txt')
#返回os.stat_result对象
print(s)
print(type(s))

#调用系统lstat函数,对于link文件，针对当前的文件名调用函数
s = os.lstat('demo.txt')
#返回os.stat_result对象
print(s)
print(type(s))

#调用系统fstat函数,该函数的参数必须为打开的文件描述符
with open('demo.txt') as f:
	s = os.fstat(f.fileno())
	#返回os.stat_result对象
	print(s)
	print(type(s))