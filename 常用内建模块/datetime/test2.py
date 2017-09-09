# -*- coding: utf-8 -*-

#datetime的加减
from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)

yesterday = now - timedelta(days=1)
print(yesterday)

print(yesterday + timedelta(hours=3))
print(now - timedelta(days=2,hours=3))

#本地时间转换为UTC时间(import timezone)

#拿到UTC时间，并强制设置时区为UTC+8:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#转换为北京时区
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

