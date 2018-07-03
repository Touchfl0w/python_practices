from multiprocessing import Process,Pipe

def f(c):
	#无数据会阻塞在这里
	data = c.recv()
	print(data)

c1,c2 = Pipe()
p = Process(target=f,args=(c2,))
p.start()
c1.send('hello world')