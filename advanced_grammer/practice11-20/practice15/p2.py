import json

python_obj = {'hello':[1,2,3],'works':18}

#将python数据结构转化为json文件
with open('demo.json','w') as wf:
	json.dump(python_obj,wf)

#从json文件中读取json字符串
with open('demo.json','r') as rf:
	#对于文本模式读取，返回值定为字符串，这里返回json字符串
	text = rf.read()
	print(type(text))
	print(text)
	#json字符串反序列化为python数据结构
	python1 = json.loads(text)
	print(type(python1))
	print(python1)

with open('demo.json','r') as rf:
	#省略中间过程，json文件直接转换为python数据结构
	python2 = json.load(rf)
	print(type(python2))
	print(python2)