#当使用函数来组织case中的代码块时，函数不包含形参，仅仅作为组织代码的一个工具
#return不是必须的，里面可以继续做一些复杂的操作
def f1():
	return x**2

def f2():
	return [k for k in range(10)]

def default():
	return "the number out of range!"

switch = {
	#使用函数作为字典的value,来组织复杂的代码块，只添加函数名，必要有括号
	#错误value:f1()
	1 : f1,
	2 : f2
}

x = 1
#default不要加括号，括号表示立即执行函数
#正确的逻辑是调用字典获取value值：某个函数，之后加括号表示执行！
#这个例子的函数有返回值，所以才有下面的赋值操作
result = switch.get(x,default)()
print(result)

x = 2
result = switch.get(x,default)()
print(result)

x = 's'
result = switch.get(x,default)()
print(result)