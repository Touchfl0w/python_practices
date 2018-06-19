import os.path
import time

#os.path内的函数内部调用os.stat 来获取文件状态，所以使用时可省略这一步！
#判断文件类型
print(os.path.isdir('demo.txt'))
print(os.path.islink('demo.txt'))
print(os.path.isfile('demo.txt'))

#判断文件大小
print(os.path.getsize('demo.txt'))

#判断修改，打开时间
print(os.path.getmtime('demo.txt'))
print(time.asctime(time.localtime(os.path.getatime('demo.txt'))))