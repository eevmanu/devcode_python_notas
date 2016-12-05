# /usr/bin/env python3
# coding=utf-8


from datetime import datetime

# Naive
dt1 = datetime.utcnow()
print(dt1)
print(isinstance(dt1, datetime))

print('=' * 50)

# Aware
dt2 = datetime.now()
print(dt2)
print(isinstance(dt2, datetime))
