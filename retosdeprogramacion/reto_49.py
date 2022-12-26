# Crea una función que sea capaz de detectar y retornar todos los handles de un texto usando solamente Expresiones Regulares. Debes crear una expresión regular para cada caso:
#- Handle usuario: Los que comienzan por "@"
#- Handle hashtag: Los que comienzan por "#"
#- Handle web: Los que comienzan por "www.", "http://", "https://" y finalizan con un dominio (.com, .es...)

import re

def detecHnadles():

    print("Introduzca el texto en el que quiere buscar:")
    text = input()
    handle_usuario = re.findall('@\w+', text)
    handle_hashtag = re.findall('#\w+', text)
    patron = r"(https://www.+[\w.%+-]+/?\w*|http://www.+[\w.%+-]+/?\w*|www.+[\w.%+-]+/?\w*)"
    handle_web = re.findall(patron, text)
    print("HANDLES DE USUARIO: {} \n HANDLES HASHTAG: {} \n HANDLES WEB: {}".format(handle_usuario, handle_hashtag, handle_web))

print(detecHnadles())