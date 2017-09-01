# -*-coding: utf-8 -*-
'a test module' #表示模块的文档注释。任何模块代码的第一个字符串都被视为模块的文档注释

import sys

def test():
	args = sys.argv#用list存储了命令行所有参数。第一个参数是该.py文件的名称。
	if len(args) == 1:
		print('Hello,world!')
	elif len(args) == 2:
		print('Hello, %s!'% args[1])
	else:
		print('Too many arguments')

if __name__ == '__main__':
	test()