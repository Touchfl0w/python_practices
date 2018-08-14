import sys
class A():
	def __init__(self,id,name):
		self.id = id
		self.name = name

class B():
	__slots__ = ['id','name']
	def __init__(self,id,name):
		self.id = id
		self.name = name
print(dir(A(1,'lisi')))
print(dir(B(2,'lisi')))
print(set(dir(A(2,'lisi'))) - set(dir(B(2,'lisi'))))
print(sys.getsizeof(A(1,'lisi')))
print(sys.getsizeof(A(1,'lisi').__dict__))