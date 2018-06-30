from threading import Thread
import requests
from xml.etree.ElementTree import ElementTree,Element
from queue import Queue

class DownloadThread(Thread):
	'''下载当前某种货币的卖单与买单'''
	def __init__(self,coin_id,queue):
		Thread.__init__(self)
		self.coin_id = coin_id
		self.queue = queue
		self.url = "https://bb.otcbtc.com/api/v2/depth?market=%s&limit=1000"
		self.url %= coin_id

	def download(self,url):
		'''下载json数据，存储为data'''
		response = requests.get(url)
		return response.json()
		
	def run(self):
		print('downloading %s' % self.coin_id)
		data = self.download(self.url)
		self.queue.put((self.coin_id,data))

class ConvertThread(Thread):
	'''把请求响应转化为xml文件'''
	def __init__(self,queue):
		Thread.__init__(self)
		self.queue = queue

	def setchildtree(self,superelement_tag,spec_dict):
		'''
		构建asks tree或者bids tree. superelement_tag是子树的根节点名，
		spec_dict是整个json字符串转换后的python字典
		'''
		e =Element(superelement_tag)
		for list_item in spec_dict[superelement_tag]:
			e1 = Element('item')
			e.append(e1)
			e2_price = Element('price')
			e2_price.text = list_item[0]
			e1.append(e2_price)
			e2_volumn = Element('volumn')
			e2_volumn.text = list_item[1]
			e1.append(e2_volumn)
		return e

	def convert(self,coin_id,spec_dict):
		'''将请求响应body的字典转换为xml文件'''
		root = Element('data')
		e_timestamp = Element('timestamp')
		#必须在xml中把数字变成字符串！否则报错：TypeError: cannot serialize 1530197213 (type int)，序列化错误！
		e_timestamp.text = str(spec_dict['timestamp'])
		root.append(e_timestamp)
		asks_childtree = self.setchildtree('asks',spec_dict)
		root.append(asks_childtree)
		bids_childtree = self.setchildtree('bids',spec_dict)
		root.append(bids_childtree)
		et = ElementTree(root)
		et.write('%s.xml' % coin_id)

	def run(self):
		while True:
			#获取队列中已经下载好的数据
			coin_id,data = self.queue.get()
			#判断队列是否已经收到哨符！
			if data == False:
				break
			print('converting %s' % coin_id)
			self.convert(coin_id,data)

if __name__ == '__main__':
	queue = Queue()
	markets = ['eosbtc','ethbtc','bchbtc','neobtc']
	threads = [DownloadThread(market,queue) for market in markets]
	for thread in threads:
		thread.start()
	ct = ConvertThread(queue)
	ct.start()
	#等待所有下载线程完毕
	for thread in threads:
		thread.join()
	#添加终止convert线程的哨符
	queue.put(('xxx',False))



