import subprocess,os

#调用check_output，执行命令并返回结果
out_bytes = subprocess.check_output(['ls','-l'])
out_text = out_bytes.decode('utf-8')
print(out_text)
#调用system函数，执行命令并将状态码返回
return_code = os.system('touch 1.txt')
print(return_code)

import stat
#返回stat对象
result = os.stat('p2.py')
#返回十进制的文件mode(包括权限等一系列信息)
print(result.st_mode)
#转换为八进制便于观察
print(oct(result.st_mode))

#找当前文件夹下的Python文件，并为文件的拥有者以及相同用户组的成员添加可执行权限
files = os.listdir('.')
for file in files:
	if file.endswith('py'):
		os.chmod(file,os.stat(file).st_mode | stat.S_IXGRP | stat.S_IXUSR)
