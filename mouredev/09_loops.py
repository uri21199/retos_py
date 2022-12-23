# ---------- LOOPS ----------- #
#While

condition_while = 0

while condition_while < 10:
    print(condition_while)
    condition_while += 1 
else:
    print("El ELSE del while")

print("Seguimos....")

while condition_while < 20:
    condition_while += 1
    if condition_while == 15:
        print("Mi condicion es 15")
        break #Corta el while
    print(condition_while)

print("Vamos con el FOR....")

#For

lista = [10, 30, 20, 40, 60, 50, 70]

for el in lista:
    print(f"Aca tenemos el elemento {el} de la lista")
    if el == 50:
        print("Encontramos el elemento 50")
        continue
else: 
    print("Terminó el bucle FOR")

print("Vamos con el...")

#Range
lista_range = list(range(10, 30, 3))
print(lista_range)


# ---------- EJERCICIOS ----------- #
#LEVEL 1
number = 0

while number <= 10:
    print(number)
    number += 1

print("Ahora el for")

for num in range(10):
    print(num)

for i in range(1, 8):
    print("#" * i)

number_2 = 0

while number_2 <= 8:
    print("#" * 8)
    number_2 += 1

for element in range(0, 11):
    print(f"{element} x {element} = {element * element}")

lista_prog = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lista in lista_prog:
    print(lista)

number_3 = 0
while number_3 <= 100:
    if (number_3 % 2) == 0:
        print(number_3)
    number_3 += 1

number_3 = 0
while number_3 <= 100:
    if (number_3 % 2) == 1:
        print(number_3)
    number_3 += 1

#LEVEL 2
number_4 = 0
for i in range(0, 101):
    number_4 = number_4 + i
    if i == 100:
        print(f"La suma total es de {number_4}")

number_5 = 0
number_6 = 0
for i in range(0, 101):
    if (i % 2) == 0:
        number_5 = number_5 + i
        if i == 100:
            print(f"La suma de total de los pares es {number_5}")
    if (i % 2) == 1:
        number_6 = number_6 + i
        if i == 99:
            print(f"La suma de total de los impares es {number_6}")


