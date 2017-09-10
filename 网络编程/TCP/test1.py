# -*- coding: utf-8 -*-
import socket

#把新浪网页首页保存到本地

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#创建链接 (传入地址和端口号)
s.connect(('www.sina.com.cn', 80))
#发送数据
s.send(b'CET / HTTP/1.1\r\n\Host:www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接收数据
buffer = []
while True:
	d = s.recv(1024)

	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

#关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

#把接受的数据写入文件
with open('sina.html', 'wb') as f:
	f.write(html)