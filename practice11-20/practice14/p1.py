import struct
#二进制结构化数据的写入与读取
#写入方法一：
bytes1 = struct.pack('5shhc5sh','ab我'.encode('utf-8'),10,15,b'q','ab我'.encode('utf-8'),10)
#注意：5s表示5byte的字符串;h:short;i:int;c:char;这些都是c语言的概念，字符串与字符char必须是bytes类型
#对应打包关系：‘ab我’：ab\xe6\x88\x91，字符'我'z占后三个byte
#10：\n\x00，因为short占两个byte，且存储方式默认为little ending(小头)，所以真实比特流为\x00\n -> \x00\x0A -> ob0000000000001010 -> 10
print(bytes1)
#读取方法一：
text = struct.unpack('5shhc5sh',bytes1)
print(text)
text = struct.unpack('5shhc',b'ab\xe6\x88\x91\x00\n\x00\x0f\x00q')
print(text)
print(struct.calcsize(('5sh')))