from functools import wraps

def deco(func):
	#带参数装饰器，指定被装饰的函数，替换的元数据任然为WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES
	#效果同上一种方法，不过更简洁
	@wraps(func)
	def wrapper(*args,**kargs):
		'''function wrapper'''
		print("in wrapper")
		func(*args,**kargs)
	return wrapper

def f1(n):
	'''function f1'''
	print(n**2)

print(f1.__name__,f1.__doc__)

@deco
def f2(n):
	'''function f2'''
	print(n**2)
print(f2.__name__,f2.__doc__)
