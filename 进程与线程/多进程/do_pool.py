# -*- coding: utf-8 -*-
#启动大量进程，用进程池的方式批量创建子进程

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)'% (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s run %0.2f seconds'% (name, (end - start)))

if __name__=='__main__':
	print('Parent process %s'% os.getpid())
	#创建Pool实例，可以同时跑4个进程
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	#调用close()之后就不会再添加新的进程
	p.close()
	p.join()
	print('All subprocesses done.')