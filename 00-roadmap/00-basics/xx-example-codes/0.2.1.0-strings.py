# -*- coding: utf-8 -*-

# String
name = "ada lovelace"
print(name)

message = 'Ada "Love"'
print(message)

message = "Ada 'Love'"
print(message)


# multiline string
name = """ada
lovelace"""
print(name)

# f-strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()}!")

# format
full_name = "{} {}".format(first_name, last_name)
print(full_name)

# tabulaciones
print("\tPython")

# saltos de línea
print("Languages:\nPython\nC\nJavaScript")

# tabulaciones y saltos de linea
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# strings indices
first_character = name[0]
print(first_character)  # output: a

last_character = name[7]
print(last_character)  # output: e

# Inmutabilidad
name = "ada love"
# name[0] = "o"  # Syntax error
name = "oda love"


# Largo de un string

cadena = "Hola, mundo!"
largo_cadena = len(cadena)
print(f"Cadena original: {cadena}")
print(f"Largo de la cadena: {largo_cadena}")

# substring
cadena = "Hola, mundo!"
subcadena = cadena[0:4]

print(f"Cadena original: {cadena}")
print(f"subcadena: {subcadena}")
