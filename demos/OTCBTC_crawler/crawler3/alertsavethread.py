import json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from threading import Thread

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