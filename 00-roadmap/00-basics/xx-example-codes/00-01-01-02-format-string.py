# -*- coding: utf-8 -*-

# .title()
formato_titulo = "hola mundo"
print(formato_titulo.title())  # Salida: Hola Mundo

# .capitalize()
capitalizar = "bienvenido a mi aplicación"
print(capitalizar.capitalize())  # Salida: Bienvenido a mi aplicación

# .lower()
convertir_minuscula = "Hola Mundo"
print(convertir_minuscula.lower())  # Salida: hola mundo

# .upper()
convertir_mayuscula = "Hola Mundo"
print(convertir_mayuscula.upper())  # Salida: HOLA MUNDO

# .swapcase()
convertir_viceversa = "Hola Mundo"
print(convertir_viceversa.swapcase())  # Salida: hOLA mUNDO

# .center(longitud[, "caracter de relleno"])
centrar_cadena = "bienvenido a mi aplicación".capitalize()
print(
    centrar_cadena.center(50, "=")
)  # Salida: ============Bienvenido a mi aplicación============
print(centrar_cadena.center(50, " "))  # Salida:             Bienvenido a mi aplicación

# .ljust(longitud[, "caracter de relleno"])
alinear_cadena_izquierda = "bienvenido a mi aplicación".capitalize()
print(
    alinear_cadena_izquierda.ljust(50, "=")
)  # Salida: Bienvenido a mi aplicación========================
print(alinear_cadena_izquierda.ljust(50, " "))  # Salida: Bienvenido a mi aplicación

# .rjust(longitud[, "caracter de relleno"])
alinear_cadena_derecha = "bienvenido a mi aplicación".capitalize()
print(
    alinear_cadena_derecha.rjust(50, "=")
)  # Salida: ========================Bienvenido a mi aplicación
print(
    alinear_cadena_derecha.rjust(50, " ")
)  # Salida:                         Bienvenido a mi aplicación

# .zfill(longitud)
anteponer_ceros = "1575"
print(anteponer_ceros.zfill(12))  # Salida: 000000001575
