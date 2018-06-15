from random import randint

d = {str(k):randint(0,10) for k in range(10)}
#d.items返回值：类集合对象
print(d.items())

#方法一：用zip将key与value列表组合成新的元组列表
#对元组列表执行sorted方法
result = zip(d.values(),d.keys())
#zip后里面的基本单元是tuple,这是永远不变的
#外边可以转换为list/set/tuple来包裹
new_result = sorted(result)
print(new_result)