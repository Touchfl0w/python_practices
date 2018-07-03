from multiprocessing import Process

def f(a,b):
	print(a*b)

p = Process(target=f,args=(1,5))
p.start()
print('main process')
p.join()
print('main1 process')