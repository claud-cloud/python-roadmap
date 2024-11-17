# -*- coding: utf-8 -*-


# .format(*args, **kwargs)
cadena = "bienvenido a mi aplicación {0}"
print(cadena.format("en Python"))  # Salida: bienvenido a mi aplicación en Python

cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"
print(
    cadena.format(100, 21, 121)
)  # Salida: Importe bruto: $100 + IVA: $21 = Importe neto: 121

cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
print(
    cadena.format(bruto=100, iva=21, neto=121)
)  # Salida: Importe bruto: $100 + IVA: $21 = Importe neto: 121
print(
    cadena.format(bruto=100, iva=100 * 21 / 100, neto=100 * 21 / 100 + 100)
)  # Salida: Importe bruto: $100 + IVA: $21.0 = Importe neto: 121.0

# .replace("subcadena a buscar", "subcadena por la cual reemplazar")
buscar = "nombre apellido"
reemplazar_por = "Juan Pérez"
print(
    "Estimado Sr. nombre apellido".replace(buscar, reemplazar_por)
)  # Salida: Estimado Sr. Juan Pérez

# .strip(["cadena"])
cadena = "  www.holabb.com  "
print(cadena.strip())  # Salida: www.holabb.com
print(cadena.strip(" "))  # Salida: www.holabb.com

# .lstrip(["caracter"])
cadena = "www.holabb.com"
print(cadena.lstrip("w."))  # Salida: holabb.com
cadena = "       www.holabb.com"
print(cadena.lstrip())  # Salida: www.holabb.com

# .rstrip(["caracter"])
cadena = "www.holabb.com    "
print(cadena.rstrip())  # Salida: www.holabb.com
