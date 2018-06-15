#lambda函数无函数名，不可直接调用，需赋值给变量
#格式：lambda parameter_list: expression
#expression不可以是赋值语句、函数等。。只能是简单表达式
f = lambda x: x**2 
print(f(2))

#map
a = [1,3,5,2,4]

def convert(x):
	return x**3
#第二个参数必须是序列，比如集合就不能使用map
y = map(convert, a)
#返回结果是map对象，必须借助map内置方法list才可以取到序列
print(y)
print(list(y))

print('*'*30)
y = map(lambda x : x**3,a)
print(list(y))
#a不会改变
print(a)