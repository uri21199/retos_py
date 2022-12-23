#Crea un programa que comprueba si los paréntesis, llaves y corchetesde una expresión están equilibrados.- Equilibrado significa que estos delimitadores se abren y cieran  en orden y de forma correcta.- Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.- Expresión balanceada: { [ ( c + d ) ] - 5 } - Expresión no balanceada: { a * ( c + d ) ] - 5 }

def equilibrio(expresion):
    palabras = expresion.split(" ")
    print(palabras)

    for i in palabras:
        if i == "{":
            for j in i:
                if j == "}":
                    continue
                else:
                    print("Hay un error.")
                    break

equilibrio("{ hola }")