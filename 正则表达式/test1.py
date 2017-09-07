# -*- coding: utf-8 -*-

#正则表达式 匹配邮箱

import re
re_email = r'^[0-9a-zA-Z]+@\w+\.com'

email = input('Enter a email address:')

if re.match(re_email, email):
	print('OK')
else:
	print('WRONG!')