# Crea una función que reciba dos array, un booleano y retorne un array.- Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.- Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def conjuntos(ar1, ar2, bool):
    conjunto = []

    if bool == True:
        for i in ar1:
            if i in ar2:
                conjunto.append(i)
        print(conjunto)
    else:
        for i in ar1:
            if i not in ar2:
                ar2.append(i)
        print(ar2)

conjuntos(["a", "b", "c"], ["a", "e", "f"], True)