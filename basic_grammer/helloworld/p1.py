
class Student():
	#类变量
	__sum = 1
	def __init__(self,name,age):
		#实例变量
		self.name = name
		self.age = age

	#实例方法
	def do_homework(this):
		#方法1（推荐，与类名不绑定！）
		print(this.__class__.__sum)
		#方法2
		print(Student.__sum)
	@classmethod
	def plus_sum(cls):
		cls.__sum += 1
		print(cls.__sum)
	@staticmethod
	def add(x,y):
		result = x + y
		print(Student.sum)

student1 = Student('wawa',18)

Student.plus_sum()
student1.do_homework()
print(Student.__sum)