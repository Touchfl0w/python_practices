s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
a = s.split(';')
print(a)
t = []
x = map(lambda x: t.extend(x.split(',')),a)
print(t)
x = list(x)
print(x)
print(t)