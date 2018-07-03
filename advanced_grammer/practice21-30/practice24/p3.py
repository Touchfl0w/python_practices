import socket

def run_sockets(addr):
	with socket.socket() as s:
		s.connect(addr)
		s.sendall(b'hello world')
		data = s.recv(1024)
		print(data)

for i in range(7):
	run_sockets(('127.0.0.1',12345))


