#Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas. - Un Anagrama consiste en formar una palabra reordenando TODAS   las letras de otra palabra inicial. - NO hace falta comprobar que ambas palabras existan. - Dos palabras exactamente iguales no son anagrama.

def anagrama(pal1, pal2):
    
    palabra1 = list(pal1)
    palabra2 = list(pal2)

    if palabra1.sort() == palabra2.sort():
        return True
    else:
        return False

print(anagrama("parra", "rrapa"))