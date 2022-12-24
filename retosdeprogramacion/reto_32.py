# Dado un listado de números, encuentra el SEGUNDO más grande.

def segundo(lista_num):
    lista = []
    for i in lista_num:
        lista.append(i)
    
    lista.sort(reverse = True)
    return lista[1]

print(segundo([1,2,3,4,5,6]))