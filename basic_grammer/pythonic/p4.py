a = (1,2,3,11,13,14)
#生成器表达式
y = (x**2 for x in a  if x < 10)
print(y)
print(tuple(y))

#对元祖使用map
y = map(lambda x: x**2,a)
print(tuple(y))
#要想过滤，还得添加filter函数！