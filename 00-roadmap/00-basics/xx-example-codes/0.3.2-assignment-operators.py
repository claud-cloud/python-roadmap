# -*- coding: utf-8 -*-

print("*** Operadores de Asignación ***")

numero = 5
print(f"Valor de numero: {numero}")

numero = 10
print(f"Valor de numero: {numero}")

cadena = "Saludos desde Python"
print(f"Valor de la cadena: {cadena}")

# Asignacion multiple
x, y, z = 5, "Hola", -9.15
print(f"Valor de x = {x}, y = {y}, z = {z}")

# Asignacion encadenada.
a = b = c = 10
print(f"Valor a = {a}, b = {b}, c = {c}")

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f"Valores iniciales x = {x}, y = {y}")

# Aplicando el concepto de asignacion multiple, intercambiamos valores
x, y = y, x
print(f"Invertir los valores x = {x}, y = {y}")

print("*** Operadores Asignacion Compuestos ***")

a, b = 10, 15
print(f"Valor inicial a: {a}, b: {b}")

# Operador compuesto de suma +=
a += b  # a = a + b
print(f"Operador a += b es: {a}")

# Operador compuesto de resta -=
a = 10  # reiniciamos la variable a
a -= b  # a = a - b
print(f"Operador a -= b es: {a}")

# Operador compuesto de multiplicacion *=
a = 10  # reiniciamos el valor de a
a *= b
print(f"Operador a *= b es: {a}")

# Operador compuesto de division /=
a = 10  # reiniciamos el valor de a
a /= b  # a = a / b
print(f"Operador a /= b es: {a:.2f}")
