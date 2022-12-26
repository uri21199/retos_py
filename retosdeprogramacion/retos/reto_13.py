# Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

def factorial(n):
    contador = 1
    for i in range(1, n + 1):
        contador = contador * i
    
    return contador

print(factorial(5))