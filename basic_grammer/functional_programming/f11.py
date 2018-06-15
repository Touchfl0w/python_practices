import time
'''
#已定义函数
def f1(x):
	print(x)
def f2(x,y,z):
	print(x,y,z)
def f3(x,y,*args):
	print(args)
def f4(x,y,**kwargs):
	print(kwargs)
'''
def deporator(func):
	def wrapper(*args,**kwargs):#概括性的可变位置参数+可变关键字参数==所有类型的参数
		print(time.time())
		func(*args,**kwargs)#参数一定要传到这里
	return wrapper
@deporator
def f1(x):
	print(x)
@deporator
def f2(x,y,z):
	print(x,y,z)
@deporator
def f3(x,y,*args):
	print(args)
@deporator
def f4(x,y,**kwargs):
	print(kwargs)
f1(3)
f2(1,2,3)
f3(1,2,'kkkk')
f4(1,2,z = 'hello')