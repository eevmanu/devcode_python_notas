# /usr/bin/env python
# coding=utf-8


tuple_ex_1 = (1, 2, 3, 4)
print(tuple_ex_1)
print(type(tuple_ex_1))
print(isinstance(tuple_ex_1, tuple))


tuple_ex_2 = (1, 2, 3)
print(tuple_ex_2)
print(type(tuple_ex_2))
print(isinstance(tuple_ex_2, tuple))


elem = tuple_ex_1[0]
print('tuple_ex_1[0]: ', elem)

# ====================================================


def f_ex():
    return 2, 4


tuple_ex_3 = f_ex()
print('f_ex(): ', tuple_ex_3)
print('type(tuple_ex_3): ', type(tuple_ex_3))
print('isinstance(): ', isinstance(tuple_ex_3, tuple))

# ====================================================

tuple_ex_1[0] = 5

del tuple_ex_1[0]
