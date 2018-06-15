#如何在列表、字典、集合中按条件筛选数据
from random import randint
from timeit import timeit
#因为for提取的变量在randint函数中未使用，所以用_,而非一个变量名
a = [randint(-10,10) for _ in range(10)]
print(a)
#方法1
b = filter(lambda x: x > 0,a)
print(list(b))
#方法2
c = [x for x in a if x > 0]
print(c)
#测试速度
print(timeit("[x for x in a if x > 0]","from __main__ import a",number=10))
print(timeit("filter(lambda x: x > 0,a)","from __main__ import a",number=10))