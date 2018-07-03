from threading import Thread
from multiprocessing import Process

def isarmstrong(n):
	'''求n是不是水仙花数，返回bool结果(无须关注具体算法）'''
	a,t = [],n
	while t > 0:
		a.append(t % 10)
		t /= 10
	k = len(a)
	return sum(x * k for x in a) == n

def findarmstrong(a,b):
	'''在a-b间寻找水仙花树'''
	result = [x for x in range(a,b) if isarmstrong(x)]
	print(result)

def run_multithreads(*args):
	'''采用多线程处理寻找水仙花树的任务，args传入的是多个查找范围'''
	threads = [Thread(target=findarmstrong,args=(a,b)) for a,b in args]
	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()

def run_multiprocess(*args):
	'''采用多线程处理寻找水仙花树的任务，args传入的是多个查找范围'''
	proceses = [Process(target=findarmstrong,args=(a,b)) for a,b in args]
	for process in proceses:
		process.start()

	for process in proceses:
		process.join()

if __name__ == '__main__':
	import time
	start = time.time()
	# run_multiprocess((200000,300000),(300000,400000))
	run_multithreads((200000,300000),(300000,400000))
	end = time.time()
	print(end-start)