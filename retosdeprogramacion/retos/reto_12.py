#Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos. Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda. NO se tienen en cuenta los espacios, signos de puntuación y tildes. Ejemplo: Ana lleva al oso la avellana.

def palindromo(cad):
    cadena = str(cad)
    string = list(cadena)

    for i in string:
        if i == " ":
            string.remove(i)

    cadena_reves = string
    cadena_reves = list(string)
    cadena_reves.reverse()
    
    if string == cadena_reves:
        return True
    else:
        return False

print(palindromo("ana lleva al oso la avellana"))
