from p2 import Human
class Student(Human):
	def __init__(self,school,name,age):
		self.school = school
		#方法二：注意，此时的__init__不包含参数self
		#super第一个参数为子类名，第二个参数为self,表示将要创建的Student对象
		super(Student,self).__init__(name,age)

	def do_homework(self):
		print("new homework")

student1 = Student('hexi xx','wakaka',18)
student1.do_homework()


