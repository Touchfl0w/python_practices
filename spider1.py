import re
import requests
import time
import json


class Spider():
	url_eos = 'https://otcbtc.com/sell_offers?currency=eos&fiat_currency=cny&payment_type=all'
	url_btc = 'https://otcbtc.com/sell_offers?currency=btc&fiat_currency=cny&payment_type=all'
	url_bch = 'https://otcbtc.com/sell_offers?currency=bch&fiat_currency=cny&payment_type=all'
	url_eth = 'https://otcbtc.com/sell_offers?currency=eth&fiat_currency=cny&payment_type=all'
	urls = {
		'eos' : url_eos,
		'btc' : url_btc,
		'bch' : url_bch,
		'eth' : url_eth
	}
	
	regex = r'<div class="recommend-card__price">([\s\S]*?)</div>'#？非贪婪

	def __fetch_content(self,url):
		r = requests.get(url)
		r_text = r.text
		return r_text
	
	def __analysis(self,r_text):
		result = re.findall(self.__class__.regex,r_text)
		result = result[0].strip()
		return result

	def __save(self,coin,time,price):
		with open('history_coin_data.json','r+') as f:
			text = f.read()
			dict1 = json.loads(text)
			dict1[coin][time] = price
			new_text = json.dumps(dict1)
			f.seek(0)
			f.write(new_text)


	def go(self):
		for k,v in self.__class__.urls.items():
			r_text = self.__fetch_content(v)
			result = self.__analysis(r_text)
			now = time.asctime( time.localtime(time.time()) )
			self.__save(k,now,result)
			print("the price of " + k + " is:￥" + result + "      " + now)
	
spider = Spider()
spider.go()
