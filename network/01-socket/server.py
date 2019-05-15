# coding: utf-8

# 服务端

import socket

sk = socket.socket()

sk.bind(('127.0.0.1', 8000))

sk.listen()

conn, addr = sk.accept()

while True:

	ret = conn.recv(1024).decode('utf-8')
	
	print(ret)
	if ret == 'bye':
		break
	info = input('>>>')
	conn.send(info.encode('utf-8'))

conn.close()
sk.close()