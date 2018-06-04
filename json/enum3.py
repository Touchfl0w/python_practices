from enum import IntEnum,unique

#一般枚举允许value重复,不会报错
class Weekdays(IntEnum):
	MONDAY = 1
	TUESDAY = 2
	WEDSDAY = 1
#加装饰器后禁止
@unique
class Weekdays1(IntEnum):
	MONDAY = 1
	TUESDAY = 2
	WEDSDAY = 3

print(type(Weekdays))