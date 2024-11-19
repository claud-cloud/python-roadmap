# -*- coding: utf-8 -*-


# .startswith("subcadena" [, posicion_inicio, posicion_fin])

comienza_con = "bienvenido a mi aplicación".capitalize()
print(comienza_con.startswith("Bienvenido"))  # Output: True
print(comienza_con.startswith("aplicación"))  # Output: False
print(comienza_con.startswith("aplicación", 10))  # Output: True

# .endswith("subcadena" [, posicion_inicio, posicion_fin])

termina_con = "bienvenido a mi aplicación".capitalize()
print(termina_con.endswith("aplicación"))  # Output: True
print(termina_con.endswith("Bienvenido"))  # Output: False
print(termina_con.endswith("Bienvenido", 0, 10))  # Output: True

# .isalnum()

es_alfanumerico = "pepegrillo 75"
print(es_alfanumerico.isalnum())  # Output: True

es_alfanumerico = "pepegrillo"
print(es_alfanumerico.isalnum())  # Output: False

es_alfanumerico = "pepegrillo75"
print(es_alfanumerico.isalnum())  # Output: True

# .isalpha()

contiene_solo_letras = "pepegrillo 75"
print(contiene_solo_letras.isalpha())  # Output: False

contiene_solo_letras = "pepegrillo"
print(contiene_solo_letras.isalpha())  # Output: True

contiene_solo_letras = "pepegrillo75"
print(contiene_solo_letras.isalpha())  # Output: False

# .isdigit()

contiene_solo_numeros = "pepegrillo 75"
print(contiene_solo_numeros.isdigit())  # Output: False

contiene_solo_numeros = "7884"
print(contiene_solo_numeros.isdigit())  # Output: True

contiene_solo_numeros = "15 84"
print(contiene_solo_numeros.isdigit())  # Output: False

contiene_solo_numeros = "75.84"
print(contiene_solo_numeros.isdigit())  # Output: False

# .islower()

contiene_solo_minusculas = "pepe grillo"
print(contiene_solo_minusculas.islower())  # Output: True

contiene_solo_minusculas = "Pepe Grillo"
print(contiene_solo_minusculas.islower())  # Output: False

contiene_solo_minusculas = "Pepegrillo"
print(contiene_solo_minusculas.islower())  # Output: False

contiene_solo_minusculas = "pepegrillo75"
print(contiene_solo_minusculas.islower())  # Output: True

# .isupper()

contiene_solo_mayusculas = "PEPE GRILLO"
print(contiene_solo_mayusculas.isupper())  # Output: True

contiene_solo_mayusculas = "Pepe Grillo"
print(contiene_solo_mayusculas.isupper())  # Output: False

contiene_solo_mayusculas = "Pepegrillo"
print(contiene_solo_mayusculas.isupper())  # Output: False

contiene_solo_mayusculas = "PEPEGRILLO"
print(contiene_solo_mayusculas.isupper())  # Output: True

# .isspace()

contiene_solo_espacios = "pepe grillo"
print(contiene_solo_espacios.isspace())  # Output: False

contiene_solo_espacios = " "
print(contiene_solo_espacios.isspace())  # Output: True

# .istitle()

contiene_formato_titulo = "Pepe Grillo"
print(contiene_formato_titulo.istitle())  # Output: True

contiene_formato_titulo = "Pepe grillo"
print(contiene_formato_titulo.istitle())  # Output: False
