def f(key,a=1,b=[]):
	'''function f'''
	print(b)
	print(key*2)
#函数名称
print(f.__name__)
#函数注释
print(f.__doc__)
#函数所属模块
print(f.__module__)
#函数的默认参数元组
print(f.__defaults__)
#修改函数参数的默认参数居然成功了，因为元组内包含列表，列表是可变对象！
#正因如此，不应该把可变对象作为参数的默认值！
f.__defaults__[1].append('100')
f(1)
##会报错，元组的元素不可被赋值
#f.__defaults__[0] = 10
#f(1)

def func1():
	a = 3
	return lambda x: a*x
g = func1()
#读取函数的闭包
#每个闭包包含多个cell对象
print(g.__closure__)
#cell对象的cell_contents属性可以读取值
print(g.__closure__[0].cell_contents) 
#函数作为对象的属性
print(func1.__dict__)