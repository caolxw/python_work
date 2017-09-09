# -*- coding: utf-8 -*-

#datetime

#获取当前时间
from datetime import datetime

now = datetime.now()
print(now)

#获取指定日期和时间
dt = datetime(2015, 2, 14, 12, 20)
print(dt)

#datetime转换成timestamp
ts = dt.timestamp()
print(ts)

#timestamp转换成datetime
dt = datetime.fromtimestamp(ts)
print(dt)

#str转换成datetime
cday = datetime.strptime('2017-6-1 18:19:50', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转换成str
print(now.strftime('%a, %b %d %H:%M:%S'))