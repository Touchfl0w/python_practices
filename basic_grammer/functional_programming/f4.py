def position(start):
	def now_position(step):
		nonlocal start
		now_position1 = start + step
		start = now_position1
		print(now_position1)
	return now_position

start = 0
f = position(start)
f(2)
f(4)
f(6)

print("-"*20)
f = position(10)
f(2)
f(4)
f(6)