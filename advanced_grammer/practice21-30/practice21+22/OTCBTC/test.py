from threading import Thread
import requests
from xml.etree.ElementTree import ElementTree,Element,tostring
from queue import Queue

def convert(coin_id,spec_dict):
		'''将请求响应body的字典转换为xml文件'''
		root = Element('data')
		e_timestamp = Element('timestamp')
		e_timestamp.text = str(spec_dict['timestamp'])
		root.append(e_timestamp)
		e_asks =Element('asks')
		root.append(e_asks)
		for list_item in spec_dict['asks']:
			e1 = Element('item')
			e_asks.append(e1)
			e2_price = Element('price')
			e2_price.text = list_item[0]
			e1.append(e2_price)
			e2_volumn = Element('volumn')
			e2_volumn.text = list_item[1]
			e1.append(e2_volumn)
		e_bids =Element('bids')
		root.append(e_bids)
		for list_item in spec_dict['bids']:
			e1 = Element('item')
			e_bids.append(e1)
			e2_price = Element('price')
			e2_price.text = list_item[0]
			e1.append(e2_price)
			e2_volumn = Element('volumn')
			e2_volumn.text = list_item[1]
			e1.append(e2_volumn)
		print(tostring(root))
		et = ElementTree(root)

		et.write('%s.xml' % coin_id)

if __name__ == '__main__':
	url = "https://bb.otcbtc.com/api/v2/depth?market=eosbtc&limit=2"
	response = requests.get(url)
	mydict = response.json()
	print(mydict)
	convert('eosbtc',mydict)