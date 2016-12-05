# /usr/bin/env python
# coding=utf-8


list_tmp = [2, 3, 4, 5]

print('list_tmp: ', list_tmp)
list_tmp.append(2)
print('list_tmp.append(2): ', list_tmp)

lista_count = list_tmp.count(2)
print('list_tmp.count(2): ', lista_count)

list_tmp.insert(2, 10)
print('list_tmp.insert(2, 10): ', list_tmp)

list_tmp.remove(2)
print('list_tmp.remove(2): ', list_tmp)

list_tmp.reverse()
print('list_tmp.reverse(): ', list_tmp)

list_tmp.sort()
print('list_tmp.sort(): ', list_tmp)

resp = list_tmp.index(10)
print('list_tmp.index(10): ', resp)
