from  urllib.request import urlretrieve
import csv
from xml.etree.ElementTree import ElementTree,Element
from threading import Thread
from queue import Queue

class DownloadThread(Thread):
	'''下载线程'''
	def __init__(self,sid,queue):
		Thread.__init__(self)
		self.sid = sid
		self.filename = 'demo{}'.format(str(sid))
		self.queue = queue

	def download(self,sid,filename):
		'''下载csv文件'''
		url = 'http://quotes.money.163.com/service/chddata.html?code=%s&start=20150104&end=20160108' % str(sid)
		response = urlretrieve(url,filename)

	def run(self):
		print("downloading %s :" % str(self.sid))
		self.download(self.sid,self.filename)
		self.queue.put(self.filename)

class ConvertThread(Thread):
	'''转换现场'''
	def __init__(self,queue):
		Thread.__init__(self)
		self.queue = queue

	def convert(self,filename):
		'''csv文件转换为xml文件'''
		with open(filename,'rt',encoding='GB2312')as rf:
			if rf:
				reader = csv.reader(rf)
				header = next(reader)
				root = Element('data')
				for row in reader:
					line = Element('row')
					root.append(line)
					for key,value in zip(header,row):
						e = Element(key)
						e.text = value
						line.append(e)
			et = ElementTree(root)
			et.write('%s.xml' % filename,encoding='utf-8')

	def run(self):
		while True:
			filename = self.queue.get()
			if filename == False:
				break
			print("converting %s :" % str(filename))
			self.convert(filename)

if __name__ == '__main__':
	#线程使用队列通信
	q = Queue()
	threads = []
	#创建并开启全部线程，包括9个下载线程和一个转换线程
	for i in range(1000001,1000010):
		t = DownloadThread(i,q)
		threads.append(t)
		t.start()
	ct = ConvertThread(q)
	ct.start()
	#等待下载线程完毕，通知转换线程结束
	for i in threads:
		i.join()
	q.put(False)


