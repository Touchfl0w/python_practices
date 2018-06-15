l = ['1','2','ss','q']
#相比于加号拼接，下列方法不仅简洁，而且占用内存小！
result = ''.join(l)
print(result)
result = 'AA'.join(l)
print(result)
#join参数是iterable即可，所以用生成器表达式生产一个generator对象（是iterable)也合理
result = ''.join((str(x) for x in range(10)))
print(result)