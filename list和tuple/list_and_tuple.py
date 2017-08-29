#-*-coding: utf-8 -*-

#列表：list 有序集合
name = ['Micheal','Bob','Tracy']

print(len(name))#list的元素个数

print('Hello,',name[0])#用索引访问list的元素
print('Hello,',name[1])
print('Hello,',name[2])
print('Hello,',name[-1])#可以用-1做索引取得最后一个元素

name.append('Adam')#添加元素到list末尾

name.insert(2,'Jack')#添加元素到指定位置

name.pop(1)#删除指定位置的元素

print(name)

moreitem = [name,'Jeason','Ruby', 123, ]#list内可以有list作为元素,元素的类型也可以不相同
print('\n',len(moreitem))
print(moreitem)
print('Hello,',moreitem[0][2])#在moreitem内取出指定的name中的元素

#元祖：tuple 初始化后不可修改 其他与list相似
t1 = (1, 2)
print('\n',t1)
t2 = (1,)#只有一个元素时，必须要加逗号
print(t2)