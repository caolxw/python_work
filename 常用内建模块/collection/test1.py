# -*- coding: utf-8 -*-

#namedtuple
from collections import namedtuple
#创建坐标
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print('(',p.x,',',p.y,')')
# namedtuple('名称',[属性list]):
Circle = namedtuple('Circle', ['x','y','r'])