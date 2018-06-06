from random import randint
from functools import reduce
game1 = {x:randint(1,3) for x in "abcdef"}
print(game1)
game2 = {x:randint(1,3) for x in "abckew"}
print(game2)
game3 = {x:randint(1,3) for x in "mnef"}
print(game3)

#注意：func不能直接为keys!!
#map函数返回值为iterator
a = map(dict.keys,[game1,game2,game3])
result = reduce(lambda x,y: x & y,a)
print(result)