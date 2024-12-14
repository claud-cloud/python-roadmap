# -*- coding: utf-8 -*-

print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(2 + 3 * 4)
print((2 + 3) * 4)
print(0.2 + 0.1)


monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes

print(monto_neto)

universe_age = 14_000_000_000

print(universe_age)

x, y, z = 0, "Hola", 20

print(x)
print(y)
print(z)
