# -*- coding: utf-8 -*-

# .join(iterable)
formato_numero_factura = ("N° 0000-0", "-0000 (ID: ", ")")
numero = "275"
numero_factura = numero.join(formato_numero_factura)
print(numero_factura)  # Salida: N° 0000-0275-0000 (ID: 275)

# .partition("separator")
tupla = "http://www.holabb.com".partition("www.")
print(tupla)  # Salida: ('http://', 'www.', 'holabb.com')

protocolo, separador, dominio = tupla
print("Protocolo: {0}\nDominio: {1}".format(protocolo, dominio))

# .split("separator")
keywords = "python, guia, curso, tutorial".split(", ")
print(keywords)  # Output: ['python', 'guia', 'curso', 'tutorial']

# .splitlines()
texto = """Linea 1
Linea 2
Linea 3
Linea 4
"""
print(texto.splitlines())  # Output: ['Linea 1', 'Linea 2', 'Linea 3', 'Linea 4']

texto = "Linea 1\nLinea 2\nLinea 3"
print(texto.splitlines())  # Output: ['Linea 1', 'Linea 2', 'Linea 3']
