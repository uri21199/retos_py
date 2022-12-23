#Comentarios
"""
Multiple comentario
en varias lineas
"""

#Escribir en consola
print('Hola Python')

#Escribir el tipo de un elemento
print(type('Hola Mundo')) #str

# ---------- EJERCICIOS ---------- #

#EJERCICIO 1
#Con python --version se chequea la versión

#EJERCICIO 2
print("Suma de 3 y 4: ", 3 + 4)
print("Resta de 3 y 4: ", 3 - 4)
print("Multiplicación de 3 y 4: ", 3 * 4)
print("División de 3 y 4: ", 3 / 4)
print("Resto de 3 y 4: ", 3 % 4)
print("Potencia de 3^4: ", 3 ** 4)

#EJERCICIO 3
print("Mi nombre es Lautaro")
print("Mi madre se llama Norma")
print("Soy de Argentina")

#EJERCICIO 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Lautaro"))

#LEVEL 3: distancia entre dos puntos
from math import sqrt

class Punto: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calcular_distancia(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

punto1 = Punto(3,2)
punto2 = Punto(6,9)

print(calcular_distancia(punto1, punto2))