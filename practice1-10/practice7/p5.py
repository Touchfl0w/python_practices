import re

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
result = re.split(r'[;|,\t]+',s)
print(result)