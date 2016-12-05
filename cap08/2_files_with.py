# /usr/bin/env python
# coding=utf-8


with open('read.txt', 'r') as f:
    lines = f.readlines()
    lines_count = len(lines)
    print('number of lines: ', lines_count)

# ====================================================

with open('write.txt', 'w') as f:
    f.write('Esta es la primera linea.\n')
    f.write('Esta es la segunda linea.\n')
    f.write('Esta es la tercera linea.\n')
    f.write('Esta es la cuarta linea.\n')
