def mysplit(s,split_keys):
	#a为初始列表,字符串转列表的方法如下
	a = [s]
	for split_key in split_keys:
		#t为分割后的暂时列表
		t = []
		#list操作是必须的，否则t.extend无法生效
		#Python中即使某个操作有返回值，也可以不赋值
		list(map(lambda x: t.extend(x.split(split_key)),a))
		##将分割后的列表赋值给初始列表，进入下一轮循环
		a = t
	return a

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
result = mysplit(s,';,|\t')
print(result)