# Echo client program
import socket
import time

HOST = 'localhost'    # The remote host
PORT = 12306       # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #sｅｎｄａｌｌ与ｒｅｃｖ均可以多次调用，即发送与接收均可不连续
    s.sendall(b'h'*2048)
    #接收数据数量可以变化，可以大于等于，甚至小于服务端发送量（服务端会报错，但客户端可以正常运行并退出）
    data1 = s.recv(4096)
    print(data1)






