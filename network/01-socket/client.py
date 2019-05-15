# coding: utf-8

import socket

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sk.connect(('127.0.0.1', 8000))

while True:

	ret = input('>>>')
	if ret == 'bye':
		sk.send(bytes(ret))
		break
	sk.send(ret.encode('utf-8'))
	res = sk.recv(1024)
	print(res.decode('utf-8'))

sk.close()