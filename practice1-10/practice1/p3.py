from random import randint

a = {randint(-20,20) for _ in range(10)}

print(a)
result = {x for x in a if x > 0}
print(result)
