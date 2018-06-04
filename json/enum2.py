from enum import Enum

class Weekdays(Enum):
	MONDAY = 1
	TUESDAY = 2
	WEDSDAY = 3

class Num_to_enum():
	a = []
	enums = []
	
	def __input_nums(self):
		for i in range(5):
			x = input("enter a num: ")
			self.__class__.a.append(int(x))
	
	@classmethod
	def __convert(cls):
		for i in cls.a:
			cls.enums.append(Weekdays(i))
	def __show_enums(self):
		print(self.__class__.enums)

	def go(self):
		self.__input_nums()
		self.__convert()
		self.__show_enums()

result = Num_to_enum()
result.go()


