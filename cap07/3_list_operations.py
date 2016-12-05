# /usr/bin/env python
# coding=utf-8


list_ex_1 = [1, 2, 3, 4]
list_ex_2 = [5, 6, 7, 8]

list_len = len(list_ex_1)
print('len(list_ex_1): ', list_len)

list_sum = list_ex_1 + list_ex_2
print('list_ex_1 + list_ex_2: ', list_sum)


list_mult = list_ex_1 * 3
print('list_ex_1 * 3: ', list_mult)

cond_1 = 1 in list_ex_1
cond_2 = 5 in list_ex_1
print('1 in list_ex_1: ', cond_1)
print('5 in list_ex_1: ', cond_2)
