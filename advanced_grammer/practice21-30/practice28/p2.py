import time 
from random import randint
import logging

def runtime(shreshold):
	def decorator(func):
		def wrapper(*args,**kargs):
			start = time.time()
			func(*args,**kargs)
			end = time.time()
			period = end - start
			if period > shreshold:
				msg = '%s:%s > %s' % (func.__name__,period,shreshold)
				logging.warn(msg)
			def setTimeout(new_shreshold):
				#nonlocal会一直向上查找
				nonlocal shreshold
				shreshold = new_shreshold
			#定义装饰器(本质是函数）的可变属性，该属性为一个函数
			# wrapper.setTimeout = setTimeout
			#更加简洁的方法为使用内置函数setattr;
			setattr(wrapper,setTimeout.__name__,setTimeout)
		return wrapper
	return decorator

@runtime(1.5)
def f1():
	print("in test")
	while randint(0,1):
		time.sleep(1)

if __name__ == "__main__":
	for _ in range(10):
		f1()
	#经过装饰器装饰后的函数f1本质上已经成为wrapper;所以下面是在调用f1的属性罢了
	f1.setTimeout(2.5)
	for _ in range(10):
		f1()