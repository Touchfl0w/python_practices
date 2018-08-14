class IntTuple(tuple):
	#覆盖tuple的内置静态方法，不需要加装饰器
	def __new__(cls,iterable):
		g = (x for x in iterable if isinstance(x,int) and x > 0)
		return super(IntTuple,cls).__new__(cls,g)

	#参数iterable必须要有，这是数据入口，随后该数据会被传递给__new__
	def __init__(self,iterable):
		print(self)
		#可选
		super(IntTuple,self).__init__()

a = IntTuple([1,44,'2',(3,5)])

