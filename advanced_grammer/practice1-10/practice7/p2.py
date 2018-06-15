a = 3
b = 4
t = [100,200]
q = []
#从下面可以知道，lambda函数可以使用非本地变量！
f = lambda x: q.append(x+a+b+t[1])
'''
上面相当于:
	def f(x):
		return q.append(x+a+b+t[1])
'''
#q.append的调用会返回None
print(f(1))
print(q)