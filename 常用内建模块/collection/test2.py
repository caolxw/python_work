# -*- coding: utf-8 -*-
#defaultdict() ：使用dict时，key不存在时，可以返回一个默认值

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abs'
print("dd['key1'] =", dd['key1'])
print("dd['key2'] =", dd['key2'])

#OrderedDict() : 使用dict时，保持key有序
from collections import OrderedDict
d = dict([('3','c'), ('2', 'b'), ('1','a')])
print(d)
od = OrderedDict([('3','c'), ('2', 'b'), ('1','a')])
print(od)

#Counter : 计数器，统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'ppruinaaaj':
	c[ch] = c[ch] + 1
print(c)