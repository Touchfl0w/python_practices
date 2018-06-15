s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
a = s.split(';')
print(a)
t = []
XXX = 'xxx'
def test(x):
	y = x.split(',')
	#作为参数的函数与普通函数并无区别，可以访问到全局变量XXX以及t
	y.append(XXX)
	return t.extend(y)
	
x = map(test,a)	
#打印出t的结果并未改变值，不是因为作为参数的test()不能访问全变量，而是因为Python3中的机制
#执行map()后仅返回map object,并未进行完整的映射计算
print(t)
#对map object 执行list操作，才会依次进行映射计算
print(list(x))
#结果证明了这一点
print(t)