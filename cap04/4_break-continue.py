# /usr/bin/env python
# coding=utf-8


# break

x = 0
while True:
    if x == 10:
        break
    x += 1

print('Salio del bucle infinito')

lista_enteros = [1, 2, 3, 4, 5]
for x in lista_enteros:
    if x == 3:
        break
    print(x)

# continue

x = 0
while x < 10:
    if x == 4:
        continue
    x += 1
    print(x)


lista_enteros = [1, 2, 3, 4, 5]
for x in lista_enteros:
    if x == 3:
        continue
    print(x)
