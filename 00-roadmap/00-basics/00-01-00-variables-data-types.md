# Variables and Data Types

Una variable es:

- Un espacio en memoria que utilizamos para almacenar datos modificables
- Cada variable tiene asociado un valor, que es la información asociada a esa variable

Añadir una variable supone un poco más de trabajo para `Python`, ya que tiene que el interprete tiene que procesar la variable.

```python
# Variable
message = "Hello Python world!"
print(message) # Output: "Hello Python world!"
```

Podemos cambiar el valor de una variable en cualquier momento y siempre se mantendrá un registro de su valor actual

```python
# New value
message = "Hello Python Crash course world!"
print(message)  # Output: "Hello Python Crash course world!"
```

A todas las variables declaradas debemos asignarle un valor inicial

## Naming and Using Variables

En `Python` existen reglas y pautas a la hora de utilizar variables.

> _Las reglas nos ayudan a no causar errores; mientras que las pautas nos ayudan a escribir código más entendible y fácil de leer_.

1. Los nombres de las variables sólo pueden contener **letras**, **números** y **guiones bajos**. Pueden comenzar con letras o guion bajo, pero no por un número:

```python
_message = "Soy una variable bien declarada."
1_message = "Malo Malo Malo" # Syntax Error
```

2. Para separar palabras solo puedo utilizar guiones bajos, los espacios no están permitidos al crear variables. También se puede utilizar `camelCase` para nombrar variables pero según las guías de estilo en `Python` es mejor utilizar `snake_case`:

```python
greeting_message = "Hello, my name is Claudio"
greeting message = "Hello, my name is Claudio" # Syntax Error
```

3. No se puede utilizar palabras reservadas como nombre de variables. Por ejemplo, no se puede utilizar `print` al nombrar una variable, esta es una **función** y una **palabra reservada** de `Python`:

```python
message = "No keyword"
print = "keyword" # Syntax Error
```

4. Cada nombre de una variable debe ser descriptivo:

```python
s_n = "Claudio" # No dice nada
student_name = "Claudio" # Da un mayor significado
```

> _Utilizar nombres de variables en minúsculas. Escribirlos en mayúsculas no es un error, pero tienen un significado especial en `Python`._

## Variables are Labels

A menudo se dice que las variables pueden ser descritas como cajas que pueden almacenar un valor dentro. Sin embargo, esta idea no es del todo precisa a como se representan internamente las variables en `Python`.

Es mejor quedarnos con la idea de que las variables son etiquetas que pueden ser asignadas a un valor. También podemos decir que una variable hace referencia a un cierto valor.

## Simple Data Types

La mayoría de los programas clasifican los distintos tipos de datos en categorías especificas. En `Python`, tenemos:

- `strings`
- `numbers`
    - `integers`
    - `floats`
- `booleans`
- `none`

## Constants

Una **constante** es una variable cuyo valor permanece invariable a lo largo de la vida de un programa. `Python` no tiene tipos de constantes incorporados, pero los programadores de `Python` usan letras mayúsculas para indicar que una variable debe ser tratada como una constante y nunca ser cambiada.

```python
MAX_CONNECTIONS = 5000
```

## Multiple Assignment

Podemos asignar valores a más de una variable utilizando una sola línea de código.

```python
a, b, c = 'string', 15, true
```