
def type(*types,**ktypes):
	def decorator(func):
		def wrapper(*args,**kargs):
			allmatch = True
			for value,_type in zip(args,types):
				if not isinstance(value,_type):
					print("value: " + str(value) + " is not " + str(_type))
					allmatch = False
					break
			if allmatch:
				func(*args,**kargs)
		return wrapper
	return decorator

@type(int,str,int)
def f1(a,b,c):
	print(a,b,c)

@type(int,int,str,tuple)
def f2(a,b,c,d):
	print(a,b,c,d)

f1("s",'qq',55)
f2(1,2,3,4)
f2(1,2,"qq",(22,33))