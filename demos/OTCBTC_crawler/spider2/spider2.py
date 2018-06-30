from threading import Thread
import requests
import time
import json
from queue import Queue
import re
from collections import namedtuple
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import schedule
import time

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

class AlertSaveThread(Thread):
	'''负责判断当前价位是否暴跌20%；将当前价位存储进json文件'''
	def __init__(self,queue,dict_cointhreshold):
		Thread.__init__(self)
		self.queue = queue
		self.dict_cointhreshold = dict_cointhreshold

	def mail(self,sender,passwd,recievers,content):
		ret = True
		try:
			msg = MIMEText(content,'plain','utf-8')
			msg['From'] = formataddr(("OTCBTC",sender))
			msg['To'] = formataddr(['付志鹏',recievers[0]])
			msg['Subject'] = "OTCBTC价格预警"
			server = smtplib.SMTP_SSL('smtp.qq.com',465)
			server.login(sender,passwd)
			server.sendmail(sender,recievers,msg.as_string())
			server.quit()
		except Exception:
			ret = False
		return ret

	def analyse(self,coin_type,threshold_price,now_price):
		'''判断价格，跌破20%则发送邮件告警，发送到邮箱：fu_zhiepng@163.com'''
		my_sender = '1754643407@qq.com'
		my_reciever = ['fu_zhipeng@163.com']
		my_passwd = 'iaytbwfmgbimeieg'
		content = "threshold price of {0} is:￥{1}\n".format(coin_type,str(threshold_price))
		content += "Notice: now price is ￥%s" % str(now_price)
		if (float(threshold_price) - float(now_price)) / float(threshold_price) >= self.dict_cointhreshold[coin_type].percentage_threshold:
			result = self.mail(my_sender,my_passwd,my_reciever,content)
			print('*'*40)
			if result:
				print(coin_type + ": " + "邮件发送成功")
			else:
				print(coin_type + ": " + "邮件发送失败")
			print('*'*40)

	def save(self,coin_type,time,price):
		'''将采集的数据保存到json文件'''
		with open('history_coin_data1.json','r+') as f:
			text = f.read()
			dict1 = json.loads(text)
			dict1[coin_type].append((time,price))
			new_text = json.dumps(dict1)
			f.seek(0)
			f.write(new_text)

	def run(self):
		while True:
			coin_type,now,lowest_price = self.queue.get()
			if lowest_price == False:
				break
			self.save(coin_type,now,lowest_price)
			#namedtuple访问使用'.'而非【】
			self.analyse(coin_type,self.dict_cointhreshold[coin_type].price_threshold,lowest_price)

def show():
	'''展示每种数字货币近三次价格记录！'''
	with open('history_coin_data1.json','r',encoding='utf-8') as rf:
		mydict = json.load(rf)
		for coin_type,time_price_pairs in mydict.items():
			print(coin_type.upper() + ":")
			#展示每种数字货币近三次价格记录！注意，json文件中至少要有三次记录，否则报错！
			#序列拆包，包括list/tuple等
			for time,price in time_price_pairs[-3:]:
				print(time + ": ￥" + price)


if __name__ == "__main__":
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








