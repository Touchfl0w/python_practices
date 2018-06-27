#多线程的使用
from  urllib.request import urlretrieve
import csv
from xml.etree.ElementTree import ElementTree,Element
from threading import Thread

def download(sid,filename):
	'''下载csv文件'''
	url = 'http://quotes.money.163.com/service/chddata.html?code=%s&start=20150104&end=20160108' % str(sid)
	response = urlretrieve(url,filename)

def convert(filename):
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

def handle(sid):
	print("downloading %s :" % str(sid))
	download(sid,'demo%s.csv' % str(sid))
	print("converting %s :" % str(sid))
	convert('demo%s.csv' % str(sid))

#方法一
threads = []
for i in range(1000001,1000010):
	#注意，args不能是（i)，因为必须是元组
	t = Thread(target=handle,args=(i,))
	threads.append(t)
	t.start()

#线程等待
for t in threads:
	t.join()

print("main thread")

#方法二
class Mythread(Thread):
	def __init__(self,sid):
		Thread.__init__(self)
		self.sid = sid

	def run(self):
		handle(self.sid)

print('*'*20)
threads = []
for i in range(1000001,1000010):
	t = Mythread(i)
	threads.append(t)
	t.start()

#线程等待
for t in threads:
	t.join()

print("main thread")
