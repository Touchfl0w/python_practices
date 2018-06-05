from random import randint
d = {x:randint(-10,10) for x in range(10)}
print(d)
#字典解析
result = {v:k for k,v in d.items() if v > 0}
print(result)
#不适合用filter