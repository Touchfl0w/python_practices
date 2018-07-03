# Echo client program
import socket
import time

HOST = 'localhost'    # The remote host
PORT = 12306       # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'h'*2048)
    data1 = s.recv(1024)
    print(data1)






