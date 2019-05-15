# coding:: utf-8
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8888))

while True:
	ret = input('>>> ')
	if ret == 'q':
		sk.send(ret.encode('utf-8'))
		break
	sk.send(ret.encode('utf-8'))
	ret = sk.recv(1024).decode('utf-8')
	print(ret)
