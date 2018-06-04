import re

a = 'C++|pytho1111n|Ja222v_a scri3pt|cs222s|HFtml|PHP'
b = 'pythonpythonpythonnpythonnnn'
# r = re.findall('\d\w{3}\s',a)
# print(r)

# r = re.findall('[a-z]{3,6}',a)
# print(r)

# r = re.findall('[a-z]{3,6}?',a)
# print(r)

# r = re.findall('python*',b)
# print(r)

# r = re.findall('python+',b)
# print(r)

# r = re.findall('python?',b)
# print(r)

# r = re.findall('^python?',b)
# print(r)
#非捕获组：返回完整匹配对象
# r = re.findall('(?:pyt..n){2}',b)
# print(r)

r = re.findall('(?:python)\1',b)
print(r)
r = re.search('(python)\1',b)
print(r)
#捕获组：仅返回捕获对象，括号内对象
# r = re.findall('(?:pyt..n){2}',b)
# print(r)
