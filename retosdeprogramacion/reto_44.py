# Crea una función que retorne el número total de bumeranes de un array de números enteros e imprima cada uno de ellos.  Un boomerang es una secuencia formada por 3 números seguidos, en el que el primero y el último son iguales, y el segundo es diferente. Por ejemplo [2, 1, 2]. - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] y [4, 2, 4]).

def boomerang(listado):
    boom = []

    for i in range(len(listado)):
        actual = listado[i]
        prev = listado[i - 1]
        sgte = listado[i + 1]
        if prev == sgte:
            boom.append([prev, actual, sgte])

    return boom

print(boomerang([1,2,1,3]))