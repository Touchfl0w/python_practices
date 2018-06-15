#闭包 = 函数 + 环境变量
a = 3

def func_pre():
	#环境变量
	a = 1
	#函数
	def func1(x):
		y = a + x
		print(y) 
	#最后一定要返回这个闭包后的函数
	return func1

f = func_pre()
f(2)

#发散一下,环境变量初始值可变的闭包
def func_pre1(a):
	#环境变量实际上为参数中的a
	#函数
	def func2(x):
		y = a + x
		print(y) 
	#最后一定要返回这个闭包后的函数
	return func2

f = func_pre1(10)
f(2)