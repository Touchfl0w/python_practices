from xml.etree.ElementTree import Element,ElementTree,tostring

#创建一个元素
e = Element('data',{'name':"wakak"})
#tostring函数以字符串的形式展现整个元素
print(tostring(e))
#修改或增加元素属性,注意属性必须是字符串
e.set('age','18')
e.set('name','wahahah')
print(tostring(e))
#修改或增加元素的text,xml是个文本文件，所以数字也要用字符串的形式写入
e.text = "123.0"
print(tostring(e))
#创建父子关系
e1 = Element('row')
e1.text = "row1"
e2 = Element('hello')
e2.text = 'hello world'
e1.append(e2)
e.append(e1)
print(tostring(e))
#创建elementTree
et = ElementTree(e)
et.write("demo1.xml")