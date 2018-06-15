def func_pre():
	#环境变量
	a = 1
	b = 2
	#函数
	def func1(x):
		y = a + x +b
		print(y) 
	#最后一定要返回这个闭包后的函数
	return func1

f = func_pre()
#返回类型是函数对象
print(type(f))
#查看该函数是不是闭包,调用函数对象的内置变量__closure__
print(f.__closure__)
#取出闭包内的环境变量
print(f.__closure__[0].cell_contents)
#环境变量会被保存为一个tuple,所以可以用index逐个取出
print(f.__closure__[1].cell_contents)
