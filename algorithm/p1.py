
from random import randint

def search(list1,target):
	low = 0
	high = len(list1) - 1
	while low < high:
		mid = int((high + low) / 2)
		guess = list1[mid]
		if guess < target: 
			low = mid + 1
		elif guess > target:
			high = mid -1
		else:
			return mid
	return None

#生成随机顺序列表
mylist = [i for i in range(1,100) if randint(0,1)]
print(mylist)
print(search(mylist,10))
print(search(mylist,11))