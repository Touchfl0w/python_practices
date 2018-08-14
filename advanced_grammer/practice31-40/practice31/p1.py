
mydict = {}

class A():
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def __enter__(self):
		mydict['a'] = self.a
		mydict['b'] = self.b
	#后三个参数是固定的，异常类型，异常实例、异常traceback对象
	def __exit__(self,exc_type,exc_val,exc_tb):
		mydict.clear()
		return True

print(mydict)
with A(3,5) as Q:
	print(mydict)
print(mydict)
