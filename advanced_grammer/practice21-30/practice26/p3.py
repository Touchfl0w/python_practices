
#求第n项的斐波那契数,从0开始
def fibonacci(n):
	if n <= 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(33))