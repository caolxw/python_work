# -*- coding: utf-8 -*-
#BytesIO可以处理二进制数据
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())