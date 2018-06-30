from retrievethread import RetrieveThread
from alertsavethread import AlertSaveThread
from show import show
from queue import Queue
import schedule
from collections import namedtuple
import time


thresholdtuple = namedtuple('thresholdtuple','price_threshold percentage_threshold')
dict_cointhreshold = {
	'eos' : thresholdtuple(50,0.2),
	'bch' : thresholdtuple(5706,0.2),
	'btc' : thresholdtuple(42685,0.1),
	'eth' : thresholdtuple(3000,0.2),
	}
queue = Queue()
def job():
	threads = [RetrieveThread(coin,queue) for coin,_ in dict_cointhreshold.items()]
	ast = AlertSaveThread(queue,dict_cointhreshold)
	for thread in threads:
		thread.start()
	ast.start()
	for thread in threads:
		thread.join()
	queue.put(("HHH","HHH",False))
	ast.join()
	show()

schedule.every(20).seconds.do(job)

while True:
	schedule.run_pending()
	time.sleep(20)