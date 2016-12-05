# /usr/bin/env python
# coding=utf-8


list_elemts = [1, 2.0, '4', True, [1, 2]]

pos = 2
print(list_elemts[pos])

list_elemts[3] = 'temp'
print(list_elemts)

del list_elemts[2]
print(list_elemts)
