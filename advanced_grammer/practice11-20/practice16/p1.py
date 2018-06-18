from xml.etree.ElementTree import parse

with open('demo.xml','r') as rf:
	#返回ElementTree对象
	et = parse(rf)
#获取根节点，返回Element对象
root = et.getroot()
print(root)
#获取某个Element对象的标签、属性以及文本
print(root.tag)
print(root.attrib)
print(root.text)
#获取某个element对象的直接子元素，返回值为element对象
print(root.getchildren())
#element对象自身可迭代
for child in root:
	#get函数返回element object 对应的attribute（‘name')的值,get获取元素属性值
	print(child.get('name'))
#find与findall一般用法默认查找直接子元素
print(root.find('country'))
print(root.findall('country'))
print(root.iterfind('country'))
for ele in root.iterfind('country'):
	print(ele)
#iter方法用来生成某个element下所有子元素的迭代器（包括非直接子元素）
print(list(root.iter()))
#指定元素的tag
print(list(root.iter('rank')))
