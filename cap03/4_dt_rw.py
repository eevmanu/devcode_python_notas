# /usr/bin/env python
# coding=utf-8


from datetime import datetime

# Lectura
date_string1 = '2016/12/01 17:15:45'
format_read = '%Y/%m/%d %H:%M:%S'
dt1 = datetime.strptime(date_string1, format_read)
print(dt1)
print(isinstance(dt1, datetime))

date_string2 = input("Ingrese una fecha: ")
dt2 = datetime.strptime(date_string2, format_read)
print(dt2)
print(isinstance(dt2, datetime))

# Escritura
dt3 = datetime.utcnow()
format_write = '%H:%M:%S %Y/%m/%d'
print(dt3.strftime(format_write))
# print(isinstance(dt3, datetime))
# 17:15:45 2016/12/01
