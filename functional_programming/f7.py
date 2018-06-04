from functools import reduce

list = [1,2,3,4,5,5,6,6]

#reduce第一个参数是function，且必须自带两个参数
#第二个参数是序列
#第三个参数是连续计算的初始值
y = reduce(lambda x,y: str(x) + str(y), list,'aaaa')
#由于reduce的功能是连续计算，故返回结果是个value,可以直接打印
print(y)
print(type(y))