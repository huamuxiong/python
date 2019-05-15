# coding:: utf-8

import socket
from multiprocessing import Process



def func(conn):
	while True:
		ret = conn.recv(1024).decode('utf-8')
		if ret == 'q':
			print('对方已退出')
			break
		print(ret)
		# info = input('>>>')
		conn.send('nihao'.encode('utf-8'))


if __name__ == '__main__':
	sk = socket.socket()
	sk.bind(('127.0.0.1', 8888))
	sk.listen()

	while True:
		conn, addr = sk.accept()
		p = Process(target=func, args=(conn, ))
		p.start()
					