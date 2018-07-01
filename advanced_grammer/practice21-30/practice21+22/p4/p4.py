from  urllib.request import urlretrieve
import csv
from xml.etree.ElementTree import ElementTree,Element
from threading import Thread
from queue import Queue
from io import StringIO
import requests

class DownloadThread(Thread):
	'''下载线程'''
	def __init__(self,sid,queue):
		Thread.__init__(self)
		self.sid = sid
		self.filename = 'demo{}'.format(str(sid))
		self.queue = queue

	def download(self,sid):
		'''下载csv文件'''
		#变化3：使用rjust来调整字符串，使得sid只输入一到两位即可
		url = 'http://quotes.money.163.com/service/chddata.html?code=1%s&start=20150104&end=20160108' % str(sid).rjust(6,'0')
		response = requests.get(url)
		#变化1：用类文件对象（内存对象）来存储csv字符串数据，而非文件
		self.data = StringIO(response.text)
		print(dir(self.data))

	def run(self):
		print("downloading %s :" % str(self.sid))
		self.download(self.sid)
		self.queue.put((self.sid,self.data))

class ConvertThread(Thread):
	'''转换现场'''
	def __init__(self,queue):
		Thread.__init__(self)
		self.queue = queue

	def convert(self,sid,data):
		'''csv文件转换为xml文件'''
		#变化1：csv模块可直接使用stringio对象来获取reader
		if data:
			reader = csv.reader(data)
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
		et.write('1%s.xml' % str(sid).rjust(6,'0'),encoding='utf-8')

	def run(self):
		while True:
			sid,data = self.queue.get()
			if data == False:
				break
			print("converting %s :" % str(sid))
			self.convert(sid,data)

if __name__ == '__main__':
	q = Queue()
	
	#变化2：使用列表推导式代替for循环,简化代码
	threads = [DownloadThread(i,q) for i in range(1,10)]
	for thread in threads:
		thread.start()
	ct = ConvertThread(q)
	ct.start()
	for i in threads:
		i.join()
	q.put((100,False))


