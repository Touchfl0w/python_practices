from random import randint

game1 = {x:randint(1,3) for x in "abcdef"}
print(game1)
game2 = {x:randint(1,3) for x in "abckew"}
print(game2)
game3 = {x:randint(1,3) for x in "mnef"}
print(game3)

#法1：for循环
res = []
for k in game1:
	if k in game2 and k in game3:
		res.append(k)

print(res)

#法2：利用dict.keys方法，返回值是个类集合对象
result = game1.keys() & game2.keys() & game3.keys()
print(result)
