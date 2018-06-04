x = [1,3,5,7,87,2,6,7,3,4,5,745,67]
#列表推导式
y = [k**2 for k in x if k < 10]
print(y)

#map函数
y = filter(lambda x: True if x < 10 else False,x)
z = map(lambda x: x**2,y)
print(list(z))

#注意：一般情况下列表推导式的功能都可以用map函数单独实现，除了上面的例子