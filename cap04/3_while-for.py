# /usr/bin/env python
# coding=utf-8


# Bloque while

a = 0
while a < 10:
    print(a)
    a = a + 1
    # a += 1

print('Valor final de a: ', a)

# Bloque for

for x in range(1, 10):
    print(x)

lista_enteros = [1, 2, 3, 4]
for item in lista_enteros:
    print('item es ', item)
