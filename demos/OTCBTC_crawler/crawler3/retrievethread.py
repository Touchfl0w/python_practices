from threading import Thread
import requests
import time
import re 

class RetrieveThread(Thread):
	'''负责抓取某个币种当前最低价的线程'''
	regex = r'<div class="recommend-card__price">([\s\S]*?)</div>'#？非贪婪

	def __init__(self,coin_type,queue):
		Thread.__init__(self)
		self.coin_type = coin_type
		self.queue = queue
		self.url = 'https://otcbtc.com/sell_offers?currency=%s&fiat_currency=cny&payment_type=all' % coin_type

	def fetch_price(self,url):
		'''获取某种数字货币当前最低价'''
		r = requests.get(url)
		r_text = r.text
		result = re.findall(self.__class__.regex,r_text)
		result = result[0].strip()
		return result

	def run(self):
		lowest_price = self.fetch_price(self.url)
		#将价格3,000中的逗号去掉
		lowest_price = re.sub(r'\,','',lowest_price)
		now = time.asctime( time.localtime(time.time()) )
		self.queue.put((self.coin_type,now,lowest_price))
