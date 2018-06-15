from random import randint

l = [randint(0,10) for _ in range(20)]
print(l)

#方法一：使用dict.fromkeys构建字典，用value来计数
#fromkeys方法构建的字典会自动去重
mydict = dict.fromkeys(l,0)
print(mydict)
#计算频率
for x in l:
	mydict[x] += 1
print(mydict)
#把字典转化为类列表，然后用sorted+key关键字按序排列
print((mydict.items()))
newdict = sorted(mydict.items(),key=lambda x:x[1])
print(newdict)
#取出频率最高的三个
newdict = newdict[-3:]
print(newdict)