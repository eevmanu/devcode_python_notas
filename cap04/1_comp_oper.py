# /usr/bin/env python
# coding=utf-8


# Operadores para comparación

a, b = 2, 4
# a, b = 4, 2
# a, b = '4', 2
# a, b = bool('4'), 2
# a, b = '4', True
# a, b = bool('4'), True

c1 = (a == b)
c2 = (a != b)
c3 = (a < b)
c4 = (a > b)
c5 = (a <= b)
c6 = (a >= b)
c7 = (a is b)
c8 = (a is not b)

print(a, ' == ', b, ': ', c1)
print(a, ' != ', b, ': ', c2)
print(a, ' < ', b, ': ', c3)
print(a, ' > ', b, ': ', c4)
print(a, ' <= ', b, ': ', c5)
print(a, ' >= ', b, ': ', c6)
print(a, ' is ', b, ': ', c7)
print(a, ' is not ', b, ': ', c8)
