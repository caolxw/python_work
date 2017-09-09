# -*- coding: utf-8 -*-
#检查任意文件是否为位图文件，如果是，打印图片大小和颜色数

import struct, os
path = input('Enter the path:')
if os.path.splitext(path)[1]=='.bmp':
	with open(path, 'rb') as f:
		s = f.read(30)
		info = struct.unpack('<ccIIIIIIHH', s)
		print('size:%d x %d'% (info[6], info[7]))
		print('color: %d'% info[-1])
else:
	print('Not a bmp picture.')