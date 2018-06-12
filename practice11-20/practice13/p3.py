
#str转bytes:仅含有ascll码的字符
a = r'123abc\n'
print(a)
print(type(a))
b = b'123abc\n'
print(b)
print(type(b))
#str转bytes:含有非ascll码，此时要借助类bytes
#bytes中表示数字、字母、控制符（ascll字符）的比特会被IDE自动解码
a = '123abc呵呵'
print(bytes(a,encoding='utf-8'))
print(bytes(a,encoding='gbk'))
#gbk向下兼容GB2312
print(bytes(a,encoding='GB2312'))
#str转bytes:含有非ascll码，此时要借助str的encode方法
print(a.encode(encoding='utf-8'))
print(a.encode(encoding='GBK'))

#bytes转str
b = b'123abc\xe5\x91\xb5\xe5\x91\xb5'
print(b.decode('utf-8'))
#对于ascll码字符集组成的字符串，直接字符表示即可，不必要写其十六进制值
b = b'\x33\x30'
print(b.decode('utf-8'))
b = b'30'
print(b.decode('utf-8'))