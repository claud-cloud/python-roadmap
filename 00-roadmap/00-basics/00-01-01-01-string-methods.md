# String Methods

En `Python` todo es un objeto y por lo tanto, cualquier variable cuyo valor sea de tipo `string`, podrá ser tratada como un subtipo del objeto `string`, por lo que dispondremos de métodos heredados por dicho subtipo.

_Como todo es un objeto, las variables de otros tipos también heredan métodos de acuerdo a su subtipo._

Tenemos métodos para: Formatear, buscar, validar y modificar `strings`. Cada método devuelve una copia del `string`.

## Format

Los métodos de formato nos ayudan a formatear `strings` de acuerdo a nuestras necesidades. Por ejemplo, hacer que la cadena esté en mayúsculas, en minúsculas, con espacios, etc.

- `.title()`: Cambia cada palabra a formato `Titlecase`. Deja la primera letra en mayúsculas y todas las demás en minúsculas.
- `.capitalize()`: convierte la primera letra en mayúscula.
- `.lower()`: Convertir una cadena a minúsculas.
- `.upper()`: Convertir una cadena a mayúsculas.
- `.swapcase()`: Convierte mayúsculas a minúsculas y viceversa.
- `.center(longitud[, "caracter de relleno"])`: Centrar un texto.
- `.ljust(longitud[, "caracter de relleno"])`: Alinear texto a la izquierda.
- `.rjust(longitud[, "caracter de relleno"])`: Alinear texto a la derecha.
- `.zfill(longitud)`: Rellenar un texto anteponiendo ceros.

## Search

En `Python` tenemos métodos para buscar apariciones de un `string` dentro de otro `string`.

- `.count("subcadena" [, posicion_inicio, posicion_fin])`: Contar cantidad de apariciones de una sub-cadena.
- `.find("subcadena" [, posicion_inicio, posicion_fin])`: Buscar una sub-cadena dentro de una cadena.

## Validation

También podemos validar `string` para saber si contiene cierta coincidencia o para saber si esta compuesto de ciertos caracteres.

- `.startswith("subcadena" [, posicion_inicio, posicion_fin])`: Saber si una cadena comienza con una sub-cadena determinada
- `.endswith("subcadena" [, posicion_inicio, posicion_fin])`: Saber si una cadena finaliza con una sub-cadena determinada
- `.isalnum()`: Saber si una cadena es alfanumérica
- `.isalpha()`: Saber si una cadena es alfabética
- `.isdigit()`: Saber si una cadena es numérica
- `.islower()`: Saber si una cadena contiene solo minúsculas
- `.isupper()`: Saber si una cadena contiene solo mayúsculas
- `.isspace()`: Saber si una cadena contiene solo espacios en blanco
- `.istitle()`: Saber si una cadena tiene "Formato De Título"

## Modify

Podemos modificar un `string` para formatear la salida de acuerdo a como nos convenga.

- `.format(*args, **kwargs)`: Sustituir un texto dinámicamente.
- `.replace("subcadena a buscar", "subcadena por la cual reemplazar")`: Reemplazar texto en una cadena.
- `.strip(["cadena"])`: Eliminar caracteres a la izquierda y derecha de una cadena.
- `.lstrip(["caracter"])`: Eliminar caracteres a la izquierda de una cadena.
- `.rstrip(["caracter"])`: Eliminar caracteres a la derecha de una cadena. Si es vacío, elimina los espacios.
- `.removeprefix("prefix")`: Elimina la cadena al inicio.

## Join and split

- `.join(iterable)`: Unir una cadena de forma iterativa.
- `.partition("separator")`: Partir una cadena en tres partes, utilizando un separador.
- `.split("separator")`: Partir una cadena en varias partes, utilizando un separador.
- `.splitlines()`: Partir una cadena en líneas.