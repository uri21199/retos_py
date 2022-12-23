### Python diario --> Link: https://pythondiario.com/2013/05/ejercicios-en-python-parte-2.html

#1: La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(lista):
    maximo = 0
    for i in lista:
        for j in lista:
            if i > j:
                maximo = i
    return maximo

print(max_in_list([1,2,3,4,5,20]))

#2: Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(lista):
    larga = ""
    for i in lista:
        for j in lista:
            if len(i) > len(j):
                larga = i
    return larga

print(mas_larga(["Perro", "Ho", "Reinado"]))

#3: Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(lista, n):
    largas = []
    for i in lista:
        if len(i) > n:
            largas.append(i)
    return(largas)

print(filtrar_palabras(["Perro", "Gato", "Ho", "H", "Tigres"], 4))

#4: Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

def cant_mayus(cadena):
    cont = 0
    for i in cadena:
        if i != i.lower():
            cont += 1
    return f"Hay {cont} mayusculas en '{cadena}'"

cadena_us = input("Ingrese una cadena de texto:")
print(cant_mayus(cadena_us))

#5: Construir un pequeño programa que convierta números binarios en enteros.
def aDecimal(numeroBin):
    numeroBin = str(numeroBin)
    decimal = 0
    exp = len (numeroBin) -1
    for i in numeroBin:
        decimal += (int(i) * 2**(exp))
        exp = exp - 1
    return decimal

print(aDecimal(10100101))

#6: Escribir un pequeño programa donde:- Se ingresa el año en curso. - Se ingresa el nombre y el año de nacimiento de tres personas.- Se calcula cuántos años cumplirán durante el año en curso.- Se imprime en pantalla.

def cumpleanios():
    a_curso = int(input("Ingrese el año en curso:"))
    
    for i in range(1, 4):
        nombre = input(f"Ingrese el nombre de la persona {i}:")
        a_nacimiento = int(input(f"Ingrese el año de nacimiento de la persona {i}:"))

        print(f"{nombre} cumplirá {a_curso - a_nacimiento} en este año {a_curso}")

cumpleanios()

#7: Definir una tupla con 10 edades de personas.Imprimir la cantidad de personas con edades superiores a 20. Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def mayor_20(tup):
    cont = 0
    for i in tup:
        if i > 20:
            cont += 1
    return f"Hay {cont} mayores a 20."

print(mayor_20((1,2,3,10,20,30,40,50,60)))

#8: Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.También se puede hacer elegir al usuario la letra a buscar.

def comienzan_a(nombres):
    contador = 0
    for i in nombres:
        if i[0].lower() == "a":
            contador += 1
    return contador

print(comienzan_a(["Agua", "Tigre"]))

#9: Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales. Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    for x in vocales:
        contador = 0
        for i in cadena:
            if i == x:
                contador += 1
        print (f"Hay {contador} {x}")

contar_vocales("Desoxirribonucleico")

#10: Escriba una función es_bisiesto() que determine si un año determinado es un añobisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def es_bisiesto():
    print ("Comprueba años bisiestos")
    a = int(input ("Escriba un años y le dire si es bisiesto: "))
    if a % 4 == 0 and (not(a % 100 == 0)):
        print ("El año", a, "es un año bisiesto porque es multiplo de 4")
    elif a % 400 == 0:
        print ("El año", a, "es un año bisiesto porque es multiplo de 400")
    else:
        print ("El año", a, "no es bisiesto")

es_bisiesto()