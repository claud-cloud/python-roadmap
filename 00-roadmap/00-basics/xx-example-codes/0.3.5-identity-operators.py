# -*- coding: utf-8 -*-

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True, porque b es el mismo objeto que a
print(a is c)  # False, aunque tienen el mismo contenido, son diferentes objetos
print(a is not c)  # True
