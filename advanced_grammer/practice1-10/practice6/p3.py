from collections import Iterator,Iterable
import requests

class WeatherIterable(Iterable):
	def __init__(self,cities):
		self.cities = cities
		self.index = 0

	def __iter__(self):
		#返回迭代器对象
		return self

	def getweather(self,city):
		r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
		dict_data = r.json()['data']['forecast'][0]
		return "%s:%s,%s" % (city,dict_data['low'],dict_data['high'])

	def __next__(self):
		if self.index == len(self.cities):
			raise StopIteration
		city = self.cities[self.index]
		self.index += 1
		return self.getweather(city)

weatheriterable = WeatherIterable([u'北京',u'南京',u'上海'])

#伪过程
#第一步：weatheriterable = weatheriterable.__iter__(),返回weatheriterable对象本身
#对象本身就有__next__方法，是的迭代器对象；这样就满足了python迭代协议
#第二步：遍历一次，就调用一次weatheritearble.__next__(),最终返回值为天气信息字符串，赋值给x
for x in weatheriterable:
	print(x)