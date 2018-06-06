from collections import Iterator,Iterable
import requests

class WeatherIterable(Iterable):
	def __init__(self,cities):
		self.cities = cities
		self.index = 0

	def __iter__(self):
		for x in range(len(self.cities)):
			city = self.cities[self.index]
			self.index += 1
			yield self.getweather(city)	

	def getweather(self,city):
		r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
		dict_data = r.json()['data']['forecast'][0]
		return "%s:%s,%s" % (city,dict_data['low'],dict_data['high'])

weatheriterable = WeatherIterable([u'北京',u'南京',u'上海'])
#伪过程
#第一步：weatheriterable = weatheriterable.__iter__(),调用生成器，返回__iter__生成器的生成器对象
#生成器对象默认拥有__iter__与__next__方法
#所以返回生成器对象也可以视作返回迭代器对象，符合python迭代协议
#第二步：遍历一次，就调用一次【迭代器对象】.__next__(),最终返回值为天气信息字符串，赋值给x
for x in weatheriterable:
	print(x)