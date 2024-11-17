# -*- coding: utf-8 -*-

# Ejercicios con strings
# Considerar que el largo de una cadena se puede obtener con len(string)

"""
    Crear un validador de nombre de usuario

    Criterios de aceptación:
        - El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
        - El nombre de usuario debe ser alfanumérico
        - Nombre de usuario con menos de 6 caracteres, retornar "El nombre de usuario debe contener al menos 6 caracteres"
        - Nombre de usuario con más de 12 caracteres, retornar "El nombre de usuario no puede contener más de 12 carácteres"
        - Nombre de usuario con caracteres distintos a los alfanuméricos, retorna "El nombre de usuario puede contener solo letras y números"
        - Nombre de usuario válido, retorna True
"""


def validate_username(username: str):
    largo_username = len(username)
    es_alfanumerico = username.isalnum()

    if largo_username < 6:
        return "El nombre de usuario debe contener al menos 6 caracteres"

    if largo_username > 12:
        return "El nombre de usuario no puede contener más de 12 carácteres"

    if not es_alfanumerico:
        return "El nombre de usuario puede contener solo letras y números"

    return "Nombre de usuario válido"


"""
    Crear un validador de contraseñas

    Criterios de aceptación:
        - La contraseña dene contener un mínimo de 8 caracteres
        - Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico
        - La contraseña no puede contener espacios en blanco
        - contraseña válida, retorna True
        - contraseña no válida, retorna "La contraseña elegida no es segura"
"""


def validate_password(password: str):
    largo_password = len(password)
    contiene_solo_minusculas = password.islower()
    contiene_solo_mayusculas = password.isupper()
    contiene_solo_numeros = password.isdigit()
    solo_es_alfanumerica = password.isalnum()
    contiene_espacios_blanco = password.find(" ") == 0

    if (
        largo_password < 8
        or contiene_solo_minusculas
        or contiene_solo_mayusculas
        or contiene_solo_numeros
        or contiene_espacios_blanco
        or solo_es_alfanumerica
    ):
        return "La contraseña elegida no es segura"

    return "La contraseña elegida si es segura"


nombre_usuario = "soyUfdsgn"
password = "sofdaaDdfda a#"

print(validate_username(nombre_usuario))
print(validate_password(password))
