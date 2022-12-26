# Crea un función que reciba un texto y retorne la vocal que más veces se repita. - Ten cuidado con algunos casos especiales. - Si no hay vocales podrá devolver vacío. 

def vocal_repetida(texto):
    VOCALS = "aeiou"

    vocales = [char for char in texto.lower() if char in VOCALS]

    if not vocales:
        return ""

    las_vocales = list(set(vocales))

    cuenta = [vocales.count(char) for char in vocales]

    indice_max = cuenta.index(max(cuenta))

    return vocales[indice_max]

print(vocal_repetida("Hola Lautaro"))