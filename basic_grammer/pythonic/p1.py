'''
#一段C++中的switch语句
switch(x){
	case 1:
		return 'a';
		break;
	case 2:
		return 'b';
		break;
	default:
		return 'default'
}
'''
x =2
#用字典实现switch语句
switch = {
	1 : 'a',
	2 : 'b',
}
'''
get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
'''
result = switch.get(x,'default')
print(result)

x = 8
result = switch.get(x,'default')
print(result)