import csv
from urllib.request import urlretrieve

#从网上下载csv文件
url = 'http://quotes.money.163.com/service/chddata.html?code=1000001&start=20150104&end=20160108'
urlretrieve(url,'pingan.csv')

#使用csv模块读取csv文件
#第一步打开文件
with open('pingan.csv','rt') as f:
	#reader是iterable，每次返回一行
	reader = csv.reader()
	print()

