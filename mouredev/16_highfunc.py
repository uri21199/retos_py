# ---------- FUNCIONES DE ORDEN SUPERIOR ----------- #

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_and_add(a, b, f_sum):
    return f_sum(a + b)

print(sum_and_add(5, 2, sum_one))
print(sum_and_add(5, 2, sum_five))

#Closures

def sum_ten(o):
    def add(v):
        return v + 10 + o
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(5)(1))

#Funciones de orden superior ya creadas
#Map()

numbers = [1,2,3,4,5]

print(list(map(sum_five, numbers)))
print(list(map(lambda n: n + 5, numbers)))

#Filter()

def filter_two(n):
    return n > 2

print(list(filter(filter_two, numbers)))
print(list(filter(lambda n: n > 2, numbers)))

#Reduce()

def sum_two_values(a, b):
    return a + b

print(reduce(sum_two_values, numbers)) #a (1) + b(2) = 3 --> a (3) + b (3) = 6 --> 6 + 4 = 10 --> 10 + 5 = 15


# ---------- EJERCICIOS ----------- #
#LEVEL 2
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
def to_upper(text):
    return text.upper()

print(list(map(to_upper, countries)))

#2
print(list(map(lambda n: n **2, numbers)))

#3
print(list(map(lambda n: n.upper(), names)))

#4
print(list(filter(lambda c: "land" in c, countries)))

#5
print(list(filter(lambda c: len(c) == 6, countries)))

#6
print(list(filter(lambda c: len(c) == 6 or len(c) > 6, countries)))

#7
print(list(filter(lambda c: c[0].lower() in "e" , countries)))

#9
def get_strings(list):
    return list(filter(lambda el: el == str, list))

print(get_strings(["tigre", 10, 20, 30, "hola", 40, 50]))



