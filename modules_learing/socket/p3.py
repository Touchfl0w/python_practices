import socket 
HOST = 'localhost'
PORT = 12306

#ｓｏｃｋｅｔ俩构造参数，第一个是地址类型、第二个是ｓｏｃｋｅｔ类型；ＡＦ_INET代表ＩＰｖ4
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	#ｓｏｃｋｅｔ允许最大1个链接
	s.listen(1)
	#accept方法返回两个值，ｃｏｎｎ是一个ｓｏｃｋｅｔ,专用来接收与发送数据，ａｄｄｒｅｓｓ是客户端的ｉｐ-port对
	#s不能直接来接受客户端的数据，只能接收连接请求
	conn,address = s.accept()
	ip,port = address
	print(ip,':',str(port),'is Connected')
	with conn as subsock:
		while True:
			#循环接收数据，每次接收１０２４ｂｙｔｅ，任意偶数即可
			#ｓｏｃｋｅｔ接收数据/发送数据都可以不连续
			#recv当没有ｄａｔａ获取时，会阻塞等待数据
			data = subsock.recv(1024)
			print(data)
			if not data:
				#当客户端中断连接，则ｒｅｃｖ会返回‘’，结束服务端
				break
			subsock.sendall(data)

