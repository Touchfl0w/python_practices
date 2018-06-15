a = [1,2,3,4,5]
b = "abcde"

list1 = map(lambda x,y: str(x) + y,a,b)
#map类内置或继承了__tuple__(),__list__()方法
print(tuple(list1))
