from multiprocessing import Process,Queue,Pipe

#进程安全Queue的基本使用
q = Queue()

def f(q):
	print('hello')
	#当队列内容为空，get操作会阻塞！，直到传入data
	print(q.get())
	print('world')

p = Process(target=f,args=(q,))
p.start()
q.put('yes it  is')