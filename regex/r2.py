import re
 
a = "pythonC++javajsC++php"
b = "pythonC++javajsc++php"

def convert1(value1):
	captured = value1.group()
	if captured == 'C++':
		return '111'
	else:
		return '222'
r = re.sub("\w\+\+",convert1,b)
print(r)
# #默认全部替换
# r = re.sub('C\+\+','go',a)
# print(r)
# #仅替换第一个
# r = re.sub('C\+\+','go',a,1)
# print(r)
# #不忽略大小写
# r = re.sub('C\+\+','go',b)
# print(r)
# #
# r = re.sub('C\+\+','go',b,0,re.I)
# print(r)
