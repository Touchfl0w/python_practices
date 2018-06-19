from tempfile import TemporaryFile,NamedTemporaryFile
import tempfile
#临时文件的默认存放地
print(tempfile.gettempdir())

#创造临时文件来存储大的数据，避免数据空耗内存;mode一般选取w+b 或 w+t
#temporary创建的临时文件在/tmp中也找不到
#返回文件对象！
f = TemporaryFile(mode='w+t')
f.write('#'*1000000)
f.close()
#使用namedtemporary创建带名字的临时文件，该文件在/tmp中找得到
#返回类文件对象
f1 = NamedTemporaryFile(mode='w+t')
print(f1.name)
f1.write('%'*10000)
#使用delete后，临时文件关闭后，文件不被立即删除
f2 = NamedTemporaryFile(mode='w+t',delete=False)
print(f2.name)
f2.write('%'*1000)
#这个地方不好验证，最好还是使用python控制台来验证临时文件的创建过程与差别
