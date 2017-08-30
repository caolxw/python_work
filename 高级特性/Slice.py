# -*- coding utf-8 -*-
#切片
L = list(range(100))

print(L)
print(L[10:20])#取出从索引10到索引20之间的元素.
print(L[:11])#从索引0开始，0可以省略
print(L[-10:])#从list的最后开始取出元素
print(L[:10:3])#前10个数，每三个取出一个
print(L[::5])#所有数，每五个取出一个

#tuple也可以切片操作
t = (1,2,3,4,5,6)
print('\n')
print(t)
print(t[::3])
#字符串也可以堪称一个list
s = 'ABCDEFG'
print('\n')
print(s)
print(s[::2])