#Crea una función que reciba un String de cualquier tipo y se encargue deponer en mayúscula la primera letra de cada palabra.- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def capitalizar(cadena):
    palabras = list(cadena.split(" "))
    cad_final = ""
    for i in palabras:
        cad_final = cad_final + " " + i.capitalize()
    return cad_final

print(capitalizar("hola perro"))
