# -*- coding: utf-8 -*-
#创建子进程
from multiprocessing import Process
import os

def run_proc(name):
	print('Run child process %s (%s)...'%(name, os.getpid()))

if __name__ == '__main__':
	print('Patent proces %s.'% os.getpid())
	p = Process(target=run_proc, args=('test',)) #创建Process实例
	print('Child process will start.')
	p.start()
	p.join() #等待子进程结束后 再继续往下运行
	print('Child process end.')