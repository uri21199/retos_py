# Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.- Utiliza el menor número de líneas para resolver el ejercicio.

def bisiestos(anio):
    lista = []
    for i in range(1, 31):
        i = anio + i*4
        lista.append(i)
    print(lista)

bisiestos(2020)
