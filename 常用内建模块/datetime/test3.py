# -*- coding: utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

#获取输入的日期和时间，以及一个时区信息，转换成timestamp

def to_timestamp(dr_str, tz_str):
	dt = datetime.strptime(dr_str, '%Y-%m-%d %H:%M:%S')
	re_utc = r'^(UTC[+-])(\d+)(:\d+)'
	m = re.match(re_utc, tz_str)
	hour = int(m.group(2))
	utc_dt = timezone(timedelta(hours=hour)) #创建时区
	dt_time = dt.replace(tzinfo=utc_dt)#强行设置为当前时区
	return dt_time.timestamp()

#test
t1 = to_timestamp('2015-6-6 08:10:30', 'UTC+7:00')
print(t1)
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t2)
assert t2 == 1433121030.0, t2

print('Pass')