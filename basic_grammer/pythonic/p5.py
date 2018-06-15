a = {1,3,643,2,1,4}

#集合推导式
y = {x**2 for x in a if x <10}
print(y)

#针对集合map
y = map(lambda x: x**2,a)
print(set(y))
#要想过滤，还得添加filter函数！