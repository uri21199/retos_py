### Listas y tuplas --> link: https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/

#1
print("1")
materias = ["Matemática", "Física", "Química", "Historia", "Lengua"]
print(materias)

#2
print("\n2")
materias = ["Matemática", "Física", "Química", "Historia", "Lengua"]
for i in materias:
    print("Yo estudio", i)

#3
print("\n3")
materias = ["Matemática", "Física", "Química", "Historia", "Lengua"]
notas = []

for i in materias:
    nota = input(f"¿Qué nota sacaste en {i}?")
    notas.append(nota)
for i in range(len(materias)):
    print(f"En {materias[i]} has sacado {notas[i]}")

#4
print("\n4")
ganadores = []
for i in range(6):
    ganadores.append(int(input("Números ganadores:")))
ganadores.sort()
print(ganadores)


#5
print("\n5")
numeros = [1,2,3,4,5,6,7,8,9,10]

for i in range(1, 11):
    print(numeros[-i], end=", ")


#6
print("\n6")
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobadas = []
for materia in materias:
    nota = float(input("¿Qué nota has sacado en " + materia + "?"))
    if nota >= 5:
        aprobadas.append(materia)
for materia in aprobadas:
    materias.remove(materia)
print("Tienes que repetir " + str(materias))

print(materias)

#7
print("\n7")
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alfabeto), 1, -1):
    if i % 3 == 0:
        alfabeto.pop(i-1)
print(alfabeto)

#8
print("\n8")
palabra = list(input("Introduce una palabra:"))
palabra_al_reves = palabra
palabra_al_reves = list(palabra_al_reves)
palabra_al_reves.reverse()

if palabra == palabra_al_reves:
    print("Es un palindromo")
else:
    print("No es palindromo")

#9
print("\n9")
palabra = input("Ingrese una palabra:")
vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
    times = 0
    for letra in palabra:
        if letra == vocal:
            times += 1
    print(f"La letra {vocal} esta {times} veces en {palabra}")

#10
print("\n10")
precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
print(min)
for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))


#11
print("\n11")
a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 


#12
print("\n12")

a = ((1, 2, 3),
    (4, 5, 6))
b = ((-1, 0),
    (0, 1),
    (1,1))
result = [[0,0],
        [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])

#13
print("\n13")
sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)

