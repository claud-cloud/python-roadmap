# -*- coding: utf-8 -*-

print(f"*** Operador and ***")

condicion1 = True
condicion2 = True

# Regresa verdadero si ambos valores a evaluar son verdaderos
resultado = condicion1 and condicion2

print(f"Resultado {condicion1} and {condicion2}: {resultado}")


print("*** Operador lógico or ***")

condicion1 = True
condicion2 = True

# El operador or regresa True si cualquiera de los operandos es True
resultado = condicion1 or condicion2

print(f"Resultado {condicion1} or {condicion2} es: {resultado}")


print("*** Operador not ***")

condicion1 = True
resultado = not condicion1

print(f"Operador not sobre {condicion1}: {resultado}")

# Revisar si una variable es cadena vacia
nombre = ""
es_cadena_vacia = not nombre
print(f"\nLa variable NO tiene ningún valor? {es_cadena_vacia}")

# Revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable
print(f"\nLa variable NO tiene ningún valor asignado? {es_variable_sin_valor}")
