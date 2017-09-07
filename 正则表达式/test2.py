# -*- coding: utf-8 -*-

#正则表达式 验证并提取名字的邮箱地址

import re

re_email = r'^([0-9a-zA-Z]+)@(\w+\.com)'

mail = input('Enter a email address:')

if re.match(re_email, mail):
	print('Right')
	print(re.match(re_email, mail).group(1))
else:
	print('Wrong')
