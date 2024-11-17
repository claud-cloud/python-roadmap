# -*- coding: utf-8 -*-


# .startswith("subcadena" [, posicion_inicio, posicion_fin])

comienza_con = "bienvenido a mi aplicación".capitalize()
print(comienza_con.startswith("Bienvenido"))  # Salida: True
print(comienza_con.startswith("aplicación"))  # Salida: False
print(comienza_con.startswith("aplicación", 10))  # Salida: True

# .endswith("subcadena" [, posicion_inicio, posicion_fin])

termina_con = "bienvenido a mi aplicación".capitalize()
print(termina_con.endswith("aplicación"))  # Salida: True
print(termina_con.endswith("Bienvenido"))  # Salida: False
print(termina_con.endswith("Bienvenido", 0, 10))  # Salida: True

# .isalnum()

es_alfanumerico = "pepegrillo 75"
print(es_alfanumerico.isalnum())  # Salida: True

es_alfanumerico = "pepegrillo"
print(es_alfanumerico.isalnum())  # Salida: False

es_alfanumerico = "pepegrillo75"
print(es_alfanumerico.isalnum())  # Salida: True

# .isalpha()

contiene_solo_letras = "pepegrillo 75"
print(contiene_solo_letras.isalpha())  # Salida: False

contiene_solo_letras = "pepegrillo"
print(contiene_solo_letras.isalpha())  # Salida: True

contiene_solo_letras = "pepegrillo75"
print(contiene_solo_letras.isalpha())  # Salida: False

# .isdigit()

contiene_solo_numeros = "pepegrillo 75"
print(contiene_solo_numeros.isdigit())  # Salida: False

contiene_solo_numeros = "7884"
print(contiene_solo_numeros.isdigit())  # Salida: True

contiene_solo_numeros = "15 84"
print(contiene_solo_numeros.isdigit())  # Salida: False

contiene_solo_numeros = "75.84"
print(contiene_solo_numeros.isdigit())  # Salida: False

# .islower()

contiene_solo_minusculas = "pepe grillo"
print(contiene_solo_minusculas.islower())  # Salida: True

contiene_solo_minusculas = "Pepe Grillo"
print(contiene_solo_minusculas.islower())  # Salida: False

contiene_solo_minusculas = "Pepegrillo"
print(contiene_solo_minusculas.islower())  # Salida: False

contiene_solo_minusculas = "pepegrillo75"
print(contiene_solo_minusculas.islower())  # Salida: True

# .isupper()

contiene_solo_mayusculas = "PEPE GRILLO"
print(contiene_solo_mayusculas.isupper())  # Salida: True

contiene_solo_mayusculas = "Pepe Grillo"
print(contiene_solo_mayusculas.isupper())  # Salida: False

contiene_solo_mayusculas = "Pepegrillo"
print(contiene_solo_mayusculas.isupper())  # Salida: False

contiene_solo_mayusculas = "PEPEGRILLO"
print(contiene_solo_mayusculas.isupper())  # Salida: True

# .isspace()

contiene_solo_espacios = "pepe grillo"
print(contiene_solo_espacios.isspace())  # Salida: False

contiene_solo_espacios = " "
print(contiene_solo_espacios.isspace())  # Salida: True

# .istitle()

contiene_formato_titulo = "Pepe Grillo"
print(contiene_formato_titulo.istitle())  # Salida: True

contiene_formato_titulo = "Pepe grillo"
print(contiene_formato_titulo.istitle())  # Salida: False
