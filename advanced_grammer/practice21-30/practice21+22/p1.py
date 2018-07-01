from  urllib.request import urlretrieve
import csv
from xml.etree.ElementTree import ElementTree,Element


def download(sid,filename):
	url = 'http://quotes.money.163.com/service/chddata.html?code=%s&start=20150104&end=20160108' % str(sid)
	response = urlretrieve(url,filename)

def convert(filename):
	with open(filename,'rt',encoding='GB2312')as rf:
		if rf:
			reader = csv.reader(rf)
			header = next(reader)
			root = Element('data')
			for row in reader:
				line = Element('row')
				root.append(line)
				for key,value in zip(header,row):
					e = Element(key)
					e.text = value
					line.append(e)
		et = ElementTree(root)
		et.write('%s.xml' % filename,encoding='utf-8')
#单进程循环
for i in range(1000001,1000010):
	print("downloading %s :" % str(i))
	download(i,'demo%s.csv' % str(i))
	print("converting %s :" % str(i))
	convert('demo%s.csv' % str(i))
