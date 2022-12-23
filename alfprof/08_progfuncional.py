### Programación funcional --> Link: https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/

#1
print("1")

def descuento(precio, porcentaje):
    return precio - precio * porcentaje/100

def iva(precio, porcentaje):
    return precio + precio * porcentaje/100

def compra(compra, func):
    total = 0
    for precio, porcentaje in compra.items():
        total += func(precio, porcentaje)
    return total

print(compra({100:20, 320:10}, descuento))
print(compra({100:20, 320:10}, iva))

#2
print("\n2")

from math import sin, cos, tan, exp, log

def funcion(f, n):
    functions = {
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "exp": exp,
    "log": log
    }
    resultados = {}

    for i in range(1, n+1):
        resultados[i] = functions[f](i)
    
    return resultados

def calculadora():
    f = input("Funcion a usar:")
    n = int(input("Veces a aplicar la funcion:"))
    for i, j in funcion(f, n).items():
        print(f"{i}\t{j}")
    return

calculadora()

#3
print("\n3")

def funcion1(lista, funcion):
    l = []

    for i in lista:
        l.append(funcion(i))
    
    return l

def cuadrado(n):
    return n + n

print(funcion1([1,2,3,4,5], cuadrado))

#4

print("\n4")

def funcion_lista(funcion, lista):
    l = []
    for i in lista:
        if funcion(i):
            l.append(i)
    return l

def menor(n):
    return n < 12

print(funcion_lista(menor, [7,8,9,11,12,13]))

#5

print("\n5")

def diccionario(frase):
    palabras = frase.split(" ")
    longitud = map(len, palabras)
    return dict(zip(palabras, longitud))

print(diccionario("Hola don pepito"))

#6
print("\n6")

def nota(n):
    if n < 4:
        return "Desaprobado"
    elif n < 7:
        return "Suficiente"
    elif n < 9:
        return "Excepcional"
    else:
        return "Excelente"

def ver_notas(notas):
    return list(map(nota, notas))

print(ver_notas([6.5, 3.2, 9.1, 10, 8.3]))

#7 y 8

print("\n7 y 8")

def nota(n):
    if n < 4:
        return "Desaprobado"
    elif n < 7:
        return "Suficiente"
    elif n < 9:
        return "Excepcional"
    else:
        return "Excelente"

def completo(notas):
    subjects = map(str.upper, notas.keys())
    grades = map(nota, notas.values())
    return dict(zip(subjects, grades))

print(completo({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))

#9

print("\n9")

def suma(x,y):
    return x + y ** 2

def modulo(v):
    from functools import reduce
    return reduce(suma, v, 0) ** 0.5

print(modulo((3,4)))

#10
print("\n10")
pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, 
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, 
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def añadir_precio(piso):
    precio = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2020 - piso['año']) / 100)
    if piso['zona'] == 'B':
        precio *= 1.5
    piso['precio'] = precio
    return piso

def busca_piso(pisos, presupuesto):
    def filtro(piso):
        return piso['precio'] <= presupuesto

    return list(filter(filtro,map(añadir_precio, pisos)))

print(busca_piso(pisos, 100000))

#11
print("\n11")

from statistics import mean, stdev

def atipico(muestra):
    media = mean(muestra)
    desviacion = stdev(muestra)
    def f(n):
        puntuacion = (n - media) / desviacion
        return (puntuacion < -3) or (puntuacion > 3)
    return f

def datos_atipicos(muestra):
    return list(filter(atipico(muestra), muestra))

print(datos_atipicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))
