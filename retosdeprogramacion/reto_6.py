# Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática. - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invertir(cadena):
    frase = list(cadena)
    frase_al_reves = list(frase)
    frase_al_reves.reverse()
    frase_al_reves = str(frase_al_reves)
    return frase_al_reves

print(invertir("Hola"))