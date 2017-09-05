# -*- coding: utf-8 -*-
#读文件
try:
	f = open('/python/helloworld.py','r')
	print(f.read())
finally:
	f.close()

# 自动调用close()方法
with open('/python/helloworld.py','r') as f:
	print(f.read())
#如果文件很小，read()一次性读取
#如果不能确定文件大小，反复调用read(size)
#如果是配置文件调用readlines() 一次性读取文件，并返回list

#读取二进制文件，比如图片，视频用'rb'

#读取非UTF-8编码文件，需要给open()函数传入encoding参数

#open()函数还可以接受一个errors参数，表示如果遇到编码错误如何处理。
#简单方式 error = 'ignore'