# Dado un array de enteros ordenado y sin repetidos, crea una función que calcule y retorne todos los que faltan entre el mayor y el menor.- Lanza un error si el array de entrada no es correcto.

def faltantes(arr):
    lista_num = []
    faltantes = []

    for i in range(len(arr)):
        lista_num.append(arr[i])
    
    lista_num.sort()

    for i in range(lista_num[0], lista_num[-1]):
        faltantes.append(i)

    return faltantes

print(faltantes([13,4,2,23,9]))
