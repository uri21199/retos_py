# ---------- FUNCIONES ----------- #

def my_func():
    print("Funcion 1")

my_func()


def sum_two(x,y):
    print(x + y)

sum_two(10,20)


def sum_return (x,y):
    return x + y
result = sum_return(10, 5)
print(result)


def sum_2 (x,y):
    sumados = x + y
    return sumados
sum_2(10,10)


def name (name, surname):
    print(f"{name} {surname}")

name(surname = "Bustos", name = "Lautaro")


def name_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

name_default(surname = "Bustos", name = "Lautaro")


# ---------- EJERCICIOS ----------- #
#LEVEL 1
#1
def add_two_numbers(x, y):
    sum = x + y
    return(sum)

print(add_two_numbers(1,2))

#2
def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    return(f"El área del círculo es {area} cuando tenga radio de {r}")

print(area_of_circle(10))

#3


#4
def convert_ctof(celsius):
    f = (celsius * 9 / 5) + 32
    return f

print(convert_ctof(10))

#5
def check_season(season):
    if season == "Enero" or season == "Febrero" or season == "Marzo":
        print("Estamos en otoño")
    elif season == "Abril" or season == "Mayo" or season == "Junio":
        print("Estamos en verano")
    elif season == "Julio" or season == "Agosto" or season == "Septiembre":
        print("Estamos en invierno")
    elif season == "Octubre" or season == "Noviembre" or season == "Diciembre":
        print("Estamos en primavera")

check_season("Enero")

#7
def solve_eq(a, b, c, x):
    eq = a * (x ** 2) + b * x + c
    return(eq)

print(solve_eq(3,4,5,2))

#8
def print_list(list):
    for i in list:
        print(i)

print_list([1, 2, 3, 4, 5])

#10
def named_cap(list):
    lista_2 = []
    for i in list:
        item = str(i).capitalize()
        lista_2.append(item)
        
    print(lista_2)

named_cap(["hola", "hola", "hola"])

#11
def add_item(list, item):
    lista_3 = []
    for i in list:
        lista_3.append(i)
    lista_3.append(item)
    print(lista_3)

add_item([1,2,3,4,5], 6)

#12
def remove_item(list, item):
    lista = []
    for i in list:
        lista.append(i)
    lista.remove(item)
    print(lista)

remove_item([1,2,3,4,5], 3)

#13
def sum_of_num(num):
    sum = 0
    for n in range(num + 1):
        sum = sum + n
    print(f"La suma de todos los numeros llegando hasta {num} es {sum}")

sum_of_num(10)

#LEVEL 2
#1
def evens_and_odds(pam):
    evens = []
    odds = []
    for i in range(0, pam + 1):
        if (i % 2) == 0:
            evens.append(i)
        if (i % 2) == 1:
            odds.append(i)
    print(len(evens))
    print(len(odds))

evens_and_odds(123)
