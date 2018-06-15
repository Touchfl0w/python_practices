from random import randint
dict1 = {str(x):randint(10,20) for x in ['wakaka','dd','ffs']}
#取最长值的方法
test = map(len,dict1.keys())
#map对象可以直接max！
max_len = max(test)
for k in dict1:
	print(k.ljust(max_len) + ":" + str(dict1[k]))

