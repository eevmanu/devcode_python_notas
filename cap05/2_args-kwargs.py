# /usr/bin/env python
# coding=utf-8


def f1(*args, **kwargs):
    print('args: ', args)
    print('type(args): ', type(args))
    print('kwargs: ', kwargs)
    print('type(kwargs): ', type(kwargs))


# f1(1, 2, 3, 4, 5)
# print('=' * 50)
# f1(param1=1, param2=2, param3=3)
