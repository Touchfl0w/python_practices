import re

with open('/var/log/dpkg.log') as f:
	text = f.read()
#注意：re.sub并不会对text做出改变，而是返回新的字符串！
new_text = re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'(\1)(\2)(\3)',text)
'''
也可以换一种写法（使用分组名称）:
new_text = re.sub(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',
	r'(\g<year>)(\g<month>)(\g<day>)',text)
'''
print(text)
print(new_text)