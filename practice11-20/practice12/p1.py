import csv
#python3中urlretrieve位置改变了
from urllib.request import urlretrieve
import chardet

#使用csv模块读取csv文件
#第一步打开文件
def convert(file_name,new_file_name):
	with open(file_name,'rt',encoding='GB2312') as f:
		reader = csv.reader(f)
		header = next(reader)
		print(header)
		with open(new_file_name,'wt',encoding='utf-8') as wf:
			writer = csv.writer(wf)
			writer.writerow(header)
			for row in reader:
				if row[0] > '2016-01-01' and int(row[11]) > 500000:
					writer.writerow(row)
			print("*************end")

#从网上下载csv文件
url = 'http://quotes.money.163.com/service/chddata.html?code=1000001&start=20150104&end=20160108'
urlretrieve(url,'pingan.csv')
convert('pingan.csv','pingan_result.csv')