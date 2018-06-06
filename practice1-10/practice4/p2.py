from random import randint

d = {str(k):randint(0,10) for k in range(10)}
#dict.items()返回一个dict_items对象，是个类集合对象，而且是个iterable
for x in d.items():
	#从结果可知，基本元素是个元组！
	print(x)
#用key参数制定排序对象
result = sorted(d.items(),key=lambda x:x[1])
print(result)