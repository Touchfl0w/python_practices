import time

def decorator1(func1):#这个参数名称可以随便起
	def wrapper():
		print(time.time())
		func1()
	return wrapper#一定要返回包装后的函数！

def f1():
	print('hello world1')

f = decorator1(f1)
#返回函数是个闭包
print(f.__closure__)
#取出唯一一个闭包的环境变量为函数f1()
print(f.__closure__[0].cell_contents)