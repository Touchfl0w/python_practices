a = []
a1= False
a2 = {}
a3 = set()
a4 = ''
a5 = 0

x = [a,a1,a2,a3,a4,a5]
for k in x:
	if k is None:
		print("wakaka")

for k in x:
	if not k:
		print('111111')

for k in x:
	if k == False:
		print('2222')

for k in x:
	if bool(k) == False:
		print('3333')