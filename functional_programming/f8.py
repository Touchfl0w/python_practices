a = [1,2,3,1,2,'2','2',3,2,45,5]
'''
对于filter函数的第一个函数参数，返回值必须是bool类型以及可以转换为
bool类型的相关类型
'''
y = filter(lambda x: False if type(x) == type('q') else True,a)
print(y)
print(list(y))

def convert(x):
	if type(x) == str:
		return False
	else:
		return True

y = filter(convert,a)
print(y)
print(list(y))
