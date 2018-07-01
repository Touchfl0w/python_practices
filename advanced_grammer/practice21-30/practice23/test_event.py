from threading import Event,Thread
import time
def f(e):
	while True:
		print('hello')
		e.wait()
		e.clear()
		print('world')

e = Event()
t = Thread(target=f,args=(e,))
t.start()
e.set()
time.sleep(1)
print('*'*40)
e.set()



