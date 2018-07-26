
#求第n项的斐波那契数,从0开始

#方法一：缓存法
#cache以值None层层传递到最底层，然后创建空字典
#cache逐层传递引用，每层的变量cache均指向同一对象！
def fibonacci(n,cache=None):
	if cache is None:
		cache = {}
	if n in cache.keys():
		return cache[n]
	if n <= 1:
		return 1
	cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache)
	return cache[n]
	
print(fibonacci(33))

#方法二：使用装饰器，一来不改变函数形式，二可利用闭包保存变量状态，比缓存法容易理解
def decorator(f):
	cache = {}
	def wrapper(*args,**kargs):
		if args not in cache.keys():
			cache[args] = f(*args,**kargs)
		return cache[args]
	return wrapper

@decorator
def fibonacci(n):
	if n <= 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(33))