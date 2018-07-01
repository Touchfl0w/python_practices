import tarfile

#1创建打包文件
#创建打包文件test.tar（可以使用路径）,模式为写；返回Tarfile对象
tar = tarfile.open('test.tar','w')
#将文件加入打包文件，可以使用绝对路径或相对路径
tar.add('1.txt')
#调用close方法，生成打包文件，位置取决于open函数中的文件名！
tar.close()

#2使用with语句，简化代码
#注意：即使add方法未生效，也会生成tar文件，只不过里面为空。
with tarfile.open('./test1.tar','w') as tar:
	tar.add('2.xml')

#3创建一个压缩打包文件
with tarfile.open('test2.tar.gz','w:gz') as tar:
	tar.add('4.xml')
	tar.add('3.json')

#4抽取所有文件
with tarfile.open('test1.tar') as tar:
	tar.extractall(path='./test')

import os.path 
#5 解压并选择性抽取文件

#创建生成器函数，挑选出文件后缀为json的tarinfo对象
#tarinfo对象表示某条被打包文件的信息
#Tarfile对象可迭代，迭代返回为tarinfo对象
def jsonfiles(tar):
	for tarinfo in tar:
		#splitext返回一个tuple(文件名，后缀)
		if os.path.splitext(tarinfo.name)[1] == '.json':
			yield tarinfo


with tarfile.open('test2.tar.gz') as tar:
	#members必须是tarinfo对象的集合
	#path不存在会自动创建
	tar.extractall(path='./test1',members=jsonfiles(tar))
