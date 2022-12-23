### Python diario --> Link: https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html

#1: Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def max(a,b):
    if a > b:
        return a
    else:
        return b

print(max(2,3))

#2: Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

print(max_de_tres(3,2,1))

#3: Definir una función que calcule la longitud de una lista o una cadena dada.

def longitud(ele):
    contador = 0
    for i in ele:
        contador += 1
    return contador

print(longitud([1,2,3,4,5,6]))
print(longitud("Hola"))

#4: Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vocal(carac):
    if carac in "aeiou":
        return True
    else:
        return False

print(vocal("a"))
print(vocal("c"))

#5: Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(lista):
    contador = 0
    for i in lista:
        contador += i
    return contador

def multip(lista):
    contador = 1
    for i in lista:
        contador *= i
    return contador

print(sum([1,2,3,4]))
print(multip([1,2,3,4]))

#6: Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    cadena = list(cadena)
    cadena.reverse()
    cadena = str(cadena)
    return cadena

print(inversa("Hola"))

#7: Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def palindromo(pal):
    palabra = list(pal)
    palabra_al_reves = palabra
    palabra_al_reves = list(palabra_al_reves)
    palabra_al_reves.reverse()

    if palabra == palabra_al_reves:
        return "Es palindromo"
    else:
        return "No es palindromo"

print(palindromo("radar"))

#8: Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

print(superposicion([1,2,3,4,5], [5,6,7,8,9]))

#9: Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(n, c):
    return int(n) * c

print(generar_n_caracteres(5,"c"))

#10: Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.

def procedimiento(n):
    for i in n:
        print( "*" * i)

procedimiento([5, 4, 9])

