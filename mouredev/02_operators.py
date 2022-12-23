# ---------- OPERADORES ----------- #

num_one = 4
num_two = 5

print("Suma: ", num_one + num_two)
print("Resta: ", num_one - num_two)
print("División: ", num_one / num_two)
print("Multiplicación: ", num_one * num_two)
print("Potencia: ", num_one ** num_two)
print("Resto: ", num_two % num_one)
print("Cociente: ", num_two // num_one)

print(num_one < num_two)
print(num_one > num_two)
print(num_one <= num_two)
print(num_one >= num_two)
print(num_one == num_two)
print(num_one != num_two)

print(3 < 4 and "hola" > "python")
print(3 < 4 or 4 < 3)
print(not(3 > 4))

# ---------- EJERCICIOS ---------- #

#EJERCICIO 4: área de un triángulo
height = input("Ingresa la altura de tu triángulo:")
base = input("Ingresa la base de tu triángulo:")

print("El área de tu triángulo es: ", int(height) * int(base) * 0.5)

#EJERCICIO 5: perimetro de un triángulo
lado_a = input("Ingresa el lado a de tu triángulo:")
lado_b = input("Ingresa el lado b de tu triángulo:")
lado_c = input("Ingresa el lado c de tu triángulo:")

print("El perímetro de tu triángulo es: ", int(lado_a) + int(lado_b) + int(lado_c))

#EJERCICIO 14: buscar palabra dentro de oración
frase = "Espero que este curso sea muy interesante"

print("muy" in frase)

#EJERCICIO 15: on en python y dragon
print("on" in "dragon" and "on" in "python")

#EJERCICIO 17:
even_ornot = input("Ingrese un número para ver si es par o no: ")
modulus = int(even_ornot) % 2

print(modulus == 0)