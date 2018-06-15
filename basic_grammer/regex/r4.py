import re

b = "pythonpythonC++javajsc++php"
c = "pythonpyth1onC++javajsc++php"
#向后引用'\'
r = re.search(r'(pyth.n)\1',b)
print(r.group())
#\1代表第一个group:(pyth.n)捕获的值,即字符串python,但是c中后面是Pyth1on，故无法匹配
#所以说向后引用不等于重复！！
r = re.search(r'(pyth.n)\1',c)
print(r)
#findall仅返回捕获值，所以这种情况下选择search方法更好！
r = re.findall(r'(python)\1',b)
print(r)
print("--------------------------------")
#坑：不使用r会报错或异常！！
r = re.findall('(python)\1',b)
print(r)
#修正
r = re.findall('(python)\\1',b)
print(r)