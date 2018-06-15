from struct import Struct
mystruct = Struct('<5shhc')
bytes1 = mystruct.pack('ab我'.encode('utf-8'),10,15,b'q')
print(bytes1)
tuple1 = mystruct.unpack(bytes1)
print(tuple1)