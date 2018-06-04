from enum import Enum 

a = lambda x: x**2
print(type(a))

class Student():
	pass
student1 = Student()
print(type(Student))
print(type(student1))

a = 'strwee'
print(type(a))

class Weekdays(Enum):
	MONDAY = 1
	TUESDAY = 2
	WEDSDAY = 3
print(type(Weekdays))
print(type(Weekdays.MONDAY))