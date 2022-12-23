# ---------- VARIABLES ----------- #
#Tipos de datos
variable_str = "String"
variable_int = 5
variable_float = 5.4
variable_bool = True
variable_list = ['Frutilla', 'Banana', 'Naranja']
variable_dict = {
    'nombre': 'Lautaro',
    'apellido': 'Bustos',
    'edad': 35
}
variable_tupla = ('Juan', 'Miguel', 'Luis') #No pueden cambiar
variable_set = {3.14, 9.15, 26.11} #No importa el orden

#Concatenación de varias variables
print(variable_dict, variable_str)

#Otra forma de concatenar
print('La variable 1 es ' + str(variable_float))

#Funciones del sist
print(len(variable_tupla))

#Varias variables en una linea
nombre, edad, apellido = "Lautaro", 23, "Bustos"
print(nombre, edad, apellido)

#Input
animal_elegido = input("Ingrese su animal:")
print(animal_elegido)

#LEVEL 2
#Ejercicio 3
if (len(variable_str) > len(str(variable_float))):
    print(variable_str, " es mas larga")

#Ejercicio 4
num_one = 5
num_two = 4

variable_total = num_one + num_two
variable_diff = num_two - num_one
variable_product = num_one * num_two
variable_division = num_one / num_two
variable_exp = num_one ** num_two
variable_floor_div = num_one // num_two

print(variable_total, variable_diff, variable_product, variable_division, variable_exp, variable_floor_div)

#EJERCICIO 5
import math
radius = 30

area_of_circle = math.pi*(radius)**2
print(area_of_circle)

circum_of_circle = math.pi* (radius*2)
print(circum_of_circle)

radius_two = int(input("Inserte su radio:"))
area_two = math.pi*(radius_two)**2
print(area_two)

help('keywords')