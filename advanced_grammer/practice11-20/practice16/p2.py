from xml.etree.ElementTree import parse

with open('demo.xml','r') as rf:
	et = parse(rf)
root = et.getroot()
print(root.findall('rank'))
#.代表当前元素，即root节点；//代表当前节点下所有子节点（包括非直接节点）
print(root.findall('.//rank'))
#..表示当前元素的父元素；/类似于Linux
print(root.findall('.//rank/..'))
#*代表所有直接子元素
print(root.findall('*/gdp'))
#带属性的元素
print(root.findall('country[@name]'))
print(root.findall('country[@name="china"]'))
#任然要指明路径
print(root.findall('rank[@updated]'))
print(root.findall('.//rank[@updated]'))
#包含某个直接子元素的元素（不支持非直接元素）
print(root.findall('country[rank]'))
#element[childelement="text"]，text即便是数字也要加引号
print(root.findall('country[rank="1"]'))
#findall找到的多个元素可以使用位置参数取出来
print(root.findall('country[rank][1]'))
print(root.findall('country[rank][2]'))
print(root.findall('country[rank][last()]'))
print(root.findall('country[rank][last()-1]'))
#注意：text文本都是string,即便看到是数字，读取后还需要进一步处理转换。
print(type(root.find('.//rank[@updated="no"]').text))