# /usr/bin/env python
# coding=utf-8


f = open('read.txt', 'r')
print(type(f))
lines = f.readlines()
lines_count = len(lines)
print('number of lines: ', lines_count)
f.close()

# ====================================================

f = open('write.txt', 'w')
f.write('Esta es la primera linea.\n')
f.write('Esta es la segunda linea.\n')
f.write('Esta es la tercera linea.\n')
f.write('Esta es la cuarta linea.\n')
f.close()
