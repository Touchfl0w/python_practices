import os 
import stat 
import time

s = os.stat('demo.txt')
print(s)
#输出文件mode
print(s.st_mode)
#使mode可读
print(stat.filemode(s.st_mode))
#判断文件类型
print(stat.S_ISDIR(s.st_mode))
print(stat.S_ISREG(s.st_mode))
print(stat.S_ISLNK(s.st_mode))

#判断文件权限
#判断文件属主是否有读权限；结果非空->True.结果为0，False；
print(s.st_mode & stat.S_IRUSR)
print(s.st_mode & stat.S_IXUSR)

#文件访问、修改时间
#返回结构化时间对象，细粒度
print(time.localtime(s.st_mtime))
#返回时间字符串！
print(time.asctime(time.localtime(s.st_atime)))

#获取文件大小,byte
print(s.st_size)