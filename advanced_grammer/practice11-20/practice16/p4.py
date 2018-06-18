#csv转xml
import csv
from xml.etree.ElementTree import Element,ElementTree

def csv_to_string(filename):
	with open(filename,'rt',encoding='utf-8') as rf:
		reader = csv.reader(rf)
		header = next(reader)
		root = Element('data')
		#下面的写法可以避免获取csv文件的行数！！
		for row in reader:
			#可以看出row可迭代！迭代返回值为list,可迭代：
			print(type(row))
			e = Element('row')
			root.append(e)
			#用到了zip函数+元组拆包
			#同样避免了计算行长度
			for tag,text in zip(header,row):
				e1 = Element(tag)
				e1.text = text
				e.append(e1)
		et = ElementTree(root)
		return et
et = csv_to_string('pingan.csv')
#此处必须表明编码格式，若省略，默认us-ascll ！！！，解析会乱码
et.write('demo2.xml',encoding='utf-8')
