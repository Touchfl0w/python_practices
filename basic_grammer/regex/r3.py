import re

b = "pythonC++javajsc++php"

#match仅从开头匹配，找到一个就结束
#match方法返回值是一个match对象，而非匹配值
r = re.match('C\+\+',b)
print(r)
r = re.match('python',b)
print(r)

print('----------------------------')
#search搜索字符串，找到即结束
#返回结果也是match对象
r = re.search('C\+\+',b)
print(r)
r = re.search('python',b)
print(r)
print(r.group())