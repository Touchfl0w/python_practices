class circle():
	def __init__(self,radius):
		self.radius = radius

	@property
	def radius(self):
		return self._radius
		
	@radius.setter
	def radius(self,value):
		if not isinstance(value,(int,float)):
			raise ValueError('wrong type')
		self._radius = value

c = circle(100)
print(c.radius)
c.radius = '1'
