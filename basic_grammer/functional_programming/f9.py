import time
'''
#假设存在三个已经编写好的函数
def f1():
	print('hello world1')
def f2():
	print('hello world2')
def f3():
	print('hello world3')
'''

#现在增加了需求，要求给上述每个函数都增加打印时间戳的功能
def decorator1(func1):#这个参数名称可以随便起
	def wrapper(x):#需要与被包装函数的参数列表形式保持一致，但名字不一定要相同
		print(time.time())
		func1(x)
	return wrapper#一定要返回包装后的函数！

@decorator1
def f1(x):
	print('hello world1')

@decorator1
def f2(y):
	print('hello world2')

@decorator1
def f3(x):
	print('hello world3')

f1(1)
f2(2)
f3(3)
