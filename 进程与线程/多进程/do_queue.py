# -*- coding: utf-8 -*-
#进程间通信

from multiprocessing import Process, Queue
import os, time, random

#写数据进程
def write(q):
	print('Process to write: %s'% os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...'% value)
		q.Put(value)
		time.sleep(random.random())

#读数据进程
def read(q):
	print('Process to read: %s'% os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.'% value)

if __name__=='__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	#启动子进程，写入
	pw.start()
	#启动子进程，读取
	pr.start()

	pw.join()

	pr.terminate()