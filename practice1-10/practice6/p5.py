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
	def __reversed__(self):
		#在这个函数内设计代码，实现反向逻辑即可
		for x in range(len(self.cities)):
			self.index -= 1
			city = self.cities[self.index]
			yield self.getweather(city)	

	def getweather(self,city):
		r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
		dict_data = r.json()['data']['forecast'][0]
		return "%s:%s,%s" % (city,dict_data['low'],dict_data['high'])

weatheriterable = WeatherIterable([u'北京',u'南京',u'上海'])

for x in weatheriterable:
	print(x)
print("*"*20)
for x in reversed(weatheriterable):
	print(x)