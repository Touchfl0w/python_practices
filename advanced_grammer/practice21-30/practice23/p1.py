import csv
from xml.etree.ElementTree import ElementTree,Element
from threading import Thread,Event
from queue import Queue
from io import StringIO
import requests
import os
import tarfile

class DownloadThread(Thread):
	'''下载线程'''
	def __init__(self,sid,queue):
		Thread.__init__(self)
		self.sid = sid
		self.filename = 'demo{}'.format(str(sid))
		self.queue = queue

	def download(self,sid):
		'''下载csv文件'''
		url = 'http://quotes.money.163.com/service/chddata.html?code=1%s&start=20150104&end=20160108' % str(sid).rjust(6,'0')
		response = requests.get(url)
		self.data = StringIO(response.text)

	def run(self):
		print("downloading %s :" % str(self.sid))
		self.download(self.sid)
		self.queue.put((self.sid,self.data))

class ConvertThread(Thread):
	'''转换线程'''
	def __init__(self,queue,cevent,tevent):
		'''转换线程与打包线程共同维护两个事件：转换事件cevent与打包事件tevent'''
		Thread.__init__(self)
		self.queue = queue
		self.cevent = cevent
		self.tevent = tevent
		#生成xml文件的计数器
		self.count = 0

	def convert(self,sid,data):
		'''csv文件转换为xml文件'''
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
				#当终止哨符发出后，可能最后的xml文件不足3个，但也要打包
				#必须先设置终止信后，后开始打包
				global tarstop
				tarstop = True
				self.tevent.set()
				break
			print("converting %s :" % str(sid))
			self.convert(sid,data)
			#每转换一个xml文件，计数器加1
			self.count += 1
			if self.count == 3:
				self.count = 0
				#通知打包线程开始打包
				self.tevent.set()
				#停止转换,要想循环使用事件，clear()需要紧跟wait()
				#注意：必须先通知打包线程，再停止转换，反过来不行
				self.cevent.wait()
				self.cevent.clear()

class TarThread(Thread):
	'''打包线程'''
	def __init__(self,cevent,tevent):
		'''转换线程与打包线程共同维护两个事件：转换事件cevent与打包事件tevent'''
		Thread.__init__(self)
		#tar包名称的初始id
		self.count = 0
		self.cevent = cevent
		self.tevent = tevent
		#任何一个循环执行的线程必须要有出口，设置为守护线程，主线程结束后，该线程自动退出，可能未完成打包任务！经测试不可行！
		# self.setDaemon(True)

	def tar(self):
		'''寻找当前文件夹下xml文件，生成打包文件，同时将源文件删除！'''
		self.count += 1
		filename = '%s.tar.gz' % str(self.count)
		with tarfile.open(filename,'w:gz') as tar:
			for file in os.listdir('.'):
				#注意函数名字：endswith不是endwith
				if file.endswith('.xml'):
					tar.add(file)
					os.remove(file)
		#如果当前文件夹下没有xml文件，但执行上一步任然会生成tar包，需要把空的tar包删除
		if not tar.members:
			os.remove(filename)

	def run(self):
		global tarstop
		while not tarstop and True:
			#阻塞等待打包命令,一旦阻塞被解除，执行完动作后应当立即调用clear(),使得下一次调用wait方法有效
			self.tevent.wait()
			self.tar()
			self.tevent.clear()

			#一旦打包完成，应当立即通知转换线程继续转换
			self.cevent.set()

if __name__ == '__main__':
	#定义线程安全队列,用于下载与转换线程间通信
	dcqueue = Queue()
	tarstop = False
	#定义转换事件与打包事件
	cevent,tevent = Event(),Event()
	#定义下载、转换、打包线程
	threads = [DownloadThread(i,dcqueue) for i in range(1,11)]
	ct = ConvertThread(dcqueue,cevent,tevent)
	tt = TarThread(cevent,tevent)
	#开启所有线程
	for thread in threads:
		thread.start()
	ct.start()
	tt.start()
	#等待下载线程执行完毕，发出转换线程的终止哨符
	for i in threads:
		i.join()
	dcqueue.put((100,False))


