# -*- coding: utf-8 -*-

#内存内读写
from io import StringIO

f = StringIO()
f.write('Hello')#返回写入的字符数
f.write(' World!')
print(f.getvalue())

t = StringIO('Hello!\n  Welcome! \n')
while True:
	s = t.readline()
	if s == '':
		break;
	print(s.strip())