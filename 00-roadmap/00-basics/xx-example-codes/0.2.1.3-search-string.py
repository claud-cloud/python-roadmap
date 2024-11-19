# -*- coding: utf-8 -*-

# .count("subcadena" [, posicion_inicio, posicion_fin])
contar_substring = "bienvenido a mi aplicación".capitalize()
print(contar_substring.count("a"))  # Output: 3

# .find("subcadena" [, posicion_inicio, posicion_fin])
buscar_substring = "bienvenido a mi aplicación".capitalize()
print(buscar_substring.find("mi"))  # Output: 13
print(buscar_substring.find("mi", 0, 10))  # Output: -1
