# -*- coding: utf-8 -*-

#根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5
import hashlib

db = {}

def get_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

def register(username, password):
	db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
	if username in db:
		if db[username] == get_md5(password + username + 'the-Salt'):
			print('登录成功')
		else:
			print('密码错误')
	else:
		print('用户不存在')
