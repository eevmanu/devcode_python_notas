# /usr/bin/env python
# coding=utf-8


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from time import time as t

# Date
d1 = date(2016, 12, 15)
print(d1)
print(isinstance(d1, date))

d2 = date(year=2016, month=12, day=15)
print(d2)
print(isinstance(d2, date))

d3 = date.today()
print(d3)
print(isinstance(d3, date))

ts = t()
d4 = date.fromtimestamp(ts)
print(d4)
print(isinstance(d4, date))

print('=' * 50)

# Time
t1 = time(20, 30, 40, 50000)
print(t1)
print(isinstance(t1, time))

t2 = time(hour=20, minute=30, second=40, microsecond=50000)
print(t2)
print(isinstance(t2, time))

print('=' * 50)

# Datetime
dt1 = datetime(2016, 12, 15, 20, 30, 40, 50000)
print(dt1)
print(isinstance(dt1, datetime))

dt2 = datetime(year=2016, month=12, day=1, hour=20, minute=30, second=40, microsecond=50000)
print(dt2)
print(isinstance(dt2, datetime))

dt3 = datetime.fromtimestamp(ts)
print(dt3)
print(isinstance(dt3, datetime))

print('=' * 50)

# Timedelta
dt4 = datetime(year=2017, month=12, day=1, hour=20, minute=30, second=40, microsecond=50000)
td1 = dt4 - dt2
print(td1)
print(isinstance(td1, timedelta))
