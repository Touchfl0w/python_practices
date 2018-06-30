import json

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