student = ('jim',18,'shanxi','china')

#方法一：伪常亮
#增添了全局变量，不推荐
NAME,AGE,PROVINCE,COUNTRY = range(4)
print(student[NAME])
print(student[AGE])

#方法二：使用namedtuple
from collections import namedtuple

#参数1：namedtuple函数返回一个Tuple子类，第一个参数是子类名称；参数2：index名称列表
Student = namedtuple('Student',['name','age','province','country'])
#Student元组类实例化,s是一个带名称的元组
s = Student('jim',18,'shanxi','china')
print(s.name) 