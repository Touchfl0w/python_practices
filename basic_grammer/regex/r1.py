import re
a = 'hellO\npython'
r = re.findall('o.p', a)
print(r)

r = re.findall('o.p', a,re.I)
print(r)

r = re.findall('o.p', a,re.I | re.S)
print(r)