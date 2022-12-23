# ---------- LIST COMPREHENSION ----------- #

original = [10, 20, 30, 40, 50, 60, 70]

lista_com = [i for i in original]
print(lista_com)

lista_com = [i for i in range(12)]
print(lista_com)

lista_com = [i + 1 for i in range(12)]
print(lista_com)

lista_com = [i + i for i in range(12)]
print(lista_com)

def sum_five(num):
    return num + 5

lista_com = [sum_five(i) for i in range(12)]
print(lista_com)


# ---------- LAMBDAS ----------- #
suma = lambda a, b: a + b
print(suma(2, 3))

mult = lambda a, b: a * b - 3
print(mult(2,3))

def prueba(c):
    return lambda a, b: a + b + c 

print(prueba(2) (3, 4))

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32


# ---------- EJERCICIOS ----------- #
#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zero =[i for i in numbers if i <= 0]
print(neg_zero)

#2
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)

#3
numeros = [(i, 1, i, i**2, i**3, ) for i in range(11)]

