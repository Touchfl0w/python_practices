import os,stat
import subprocess

def show_status(path='.'):
	output_bytes = subprocess.check_output(['ls','-l',path])
	output_text = output_bytes.decode('utf-8')
	print(output_text)

show_status()
#找当前文件夹下的Python文件，并为文件的拥有者以及相同用户组的成员添加可执行权限
files = os.listdir('.')
for file in files:
	if file.endswith('py'):
		os.chmod(file,os.stat(file).st_mode | stat.S_IXGRP | stat.S_IXUSR)

show_status()