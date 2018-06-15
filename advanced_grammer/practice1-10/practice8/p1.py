import os

files = os.listdir('/home/openlab')
print(files)
for x in files:
	if x.endswith('.py'):
		print('*'*20 + x)
	#注意：不是elseif
	#startswith与endswith使用多个参数时，只能用元组将参数括起来，参数间关系为或！
	elif x.startswith(('.s','.x')):
		print('#'*20 + x)


