# Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole únicamente el tamaño del lado. - Aquí puedes ver rápidamente cómo se calcula el triángulo: https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif

tamaño = int(input("Tamaño del lado: "))
lista = []

for i in range(tamaño):
    lista.append([])
    lista[i].append(1)

    for j in range(1, i):
        lista[i].append(lista[i - 1][j - 1] + lista[i - 1][j])

    if(tamaño != 0):
        lista[i].append(1)

for i in range(tamaño):
    print(" " * (tamaño - i), end = " ", sep = " ")
    
    for j in range(0, i + 1):
        print('{0:5}'.format(lista[i][j]), end = " ", sep = " ")
    print()