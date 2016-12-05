# /usr/bin/env python
# coding=utf-8


def f2(param1, param2, param3=None, *args, **kwargs):
    print('param1: ', param1)
    print('param2: ', param2)
    print('param3: ', param3)
    print('args: ', args)
    print('kwargs: ', kwargs)


# f2(1)
# f2(1, 2)
# f2(1, 2, 3)
# f2(1, 2, 3, 4)
# f2(param1=1)
# f2(param1=1, param2=2)
# f2(param1=1, param2=2, param3=3)
# f2(param1=1, param2=2, param3=3, param4=4)
