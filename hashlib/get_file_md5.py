

import hashlib
class GetFileMd5:
	def __init__(self, filename):
		self.filename = filename

	# 将读的内容摘要
	def md5_update(self, content):
		self.md5 = hashlib.md5()
		self.md5.update(bytes(content, encoding='utf-8'))

	# 读文件
	def get_file_md5(self):
		with open(self.filename, encoding='utf-8') as f:
			while True:
				content = f.readline()
				if not content:
					break
				self.md5_update(content.strip())
		return self.get_hexdigest()

	# 获取最后的文件的摘要
	def get_hexdigest(self):
		return self.md5.hexdigest()

if __name__ == '__main__':

	print('这个功能是获取文件的MD5摘要')
	message = '请输入文件名或路径： '
	while True:
		input_content = input(message)
		if input_content.lower() == 'n':
			import sys
			sys.exit('\n已退出')
		if input_content.lower() == 'y':
			message = '请输入文件名或路径： '
			continue
		import os
		if os.path.isfile(input_content) and os.path.exists(input_content):
			get_file = GetFileMd5(input_content)
			get_md5 = get_file.get_file_md5()
			print('文件的摘要是： ', get_md5)
			message = '是否继续[Y/N]: '
		else:
			print('您的输入有误！\n')
			message = '请重新输入： '

