import socket
from concurrent.futures import ThreadPoolExecutor

HOST = 'localhost'
PORT = 12345

def handle_request(conn):
	with conn as subsock:
		while True:
			data = subsock.recv(1024)
			if not data:
				break
			subsock.sendall(data)

def server(address):
	pool = ThreadPoolExecutor(10)
	ip,port = address
	with socket.socket() as s:
		s.bind(address)
		s.listen(5)
		while True:
			conn,address = s.accept()
			print('Client ' + ip + ":" + str(port) + ' connected')
			pool.submit(handle_request,conn)

server(('localhost',12345))

