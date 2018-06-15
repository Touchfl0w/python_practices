with open('write.txt','wt',encoding='utf-8')as wf:
	#write参数是str,返回值为写入的byte数
	print(wf.write('wakaka服装店'))
	#查看方法
	print(dir(wf))
	#tell、seek可以使用，不推荐
	print(wf.tell())
	wf.seek(0)
	print(wf.tell())
