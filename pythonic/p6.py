a = {
	1 : "hello",
	2 : 'world'
}
#字典推导式
y = {v:str(k) for k,v in a.items()}
print(y)
#针对字典map
y = map(lambda x: str(x),a.keys())
print(list(y))

y = map(lambda x: x,a.values())
print(tuple(y))

y = map(lambda x,y: str(x)+y,a.keys(),a.values())
print(set(y))