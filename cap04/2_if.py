# /usr/bin/env python
# coding=utf-8


# Bloque if

# Tipo 1

if True:
    print("Hola Mundo 1")

if False:
    print("Hola Mundo 2")

if 2 < 4:
    print("Hola Mundo 3")

if 2 > 4:
    print("Hola Mundo 4")

if (2 < 4):
    print("Hola Mundo 5")

# Tipo 2

cond = True
cond = False

if cond:
    print('Condicion verdadera')
else:
    print('Condicion falsa')

# Tipo 3

a, b = 2, 4

if a < b:
    print('variable B es mayor que A')
elif a == b:
    print('variable B es igual que A')
else:
    print('variable B es menor que A')
