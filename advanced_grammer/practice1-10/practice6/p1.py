import requests
import pprint
#测试代码
# r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%E5%8C%97%E4%BA%AC')
# pprint.pprint(r.json())

#实现一个迭代器
from collections import Iterator

#构造迭代器
class WeatherIterator(Iterator):
	def __init__(self,cities):
		self.cities = cities
		self.index = 0

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
		

#生成迭代器对象		
weatheriterator = WeatherIterator([u'北京',u'南京',u'上海'])
#迭代器对象调用next()方法
print(weatheriterator.__next__())
print(weatheriterator.__next__())
print(weatheriterator.__next__())
#没有定义__iter__方法，不是可迭代对象，所以暂时无法for in
