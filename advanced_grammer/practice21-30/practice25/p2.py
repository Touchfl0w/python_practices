from multiprocessing import Process

x = 1
def f():
	global x
	x = 7

p = Process(target=f)
p.start()
p.join()
print(x)