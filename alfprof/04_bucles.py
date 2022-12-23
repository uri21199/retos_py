### Bucles --> link: https://aprendeconalf.es/docencia/python/ejercicios/bucles/

#1
palabra = input("Palabra:")

for i in range(11):
    print(palabra)

#2
edad = int(input("Edad:"))
for i in range (edad + 1):
    print(i)

#3
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")

#4
n2 = int(input("Introduce un número positivo: "))
for i in range(n2, -1, -1):
    print(i, end=", ")

#5
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))

#6
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")

#7
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

#8
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

#9
key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")

#10
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

#11
word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])

#12
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

#13
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)