# -*- coding: utf-8 -*-
#写文件
with open('/python/test.txt','w') as f:
	f.write('hello world!')

#书写二进制文件 'wb'

with open('/python/test.txt','r') as f:
	print(f.read())