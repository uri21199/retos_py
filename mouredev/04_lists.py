# ---------- LISTAS ----------- #
my_list = list()
my_list_2 = [10, 20, 30, 40, 50, 60, 20]
print(len(my_list_2))
print(my_list_2[0])
print(my_list_2[-1])
print(my_list_2[-3])
print(my_list_2[2:4]) #El inicial incluido, el final NO incluido
print(my_list_2.count(20)) #Cuenta cantidad de elementos repetidos

list_3 = ["Lautaro", 23]
name, age = list_3
print(age)

print(my_list_2 + list_3)

my_list_2.append(80) #Agregar cosas a la lista
print(my_list_2)

my_list_2.insert(1,5) #(pos, ele)
print(my_list_2)
my_list_2[1] = 7
print(my_list_2)

my_list_new = my_list_2.copy()

my_list_2.remove(80) #primer ele encontrado
print(my_list_2)

my_list_2.pop() #elimina el ultimo o (pos)
print(my_list_2)

my_list_2.clear() #vacia lista
print(my_list_2)

print(my_list_new)
my_list_new.reverse()
print(my_list_new)

my_list_new.sort() #ordenar
print(my_list_new)

del my_list_new[2] #eliminar con del
print(my_list_new)

list_3.extend(my_list_new)
print(list_3)

print(list_3.index("Lautaro"))

# ---------- EJERCICIOS ----------- #
#EJERCICIO 6 - 25
it_companies = ["Facebook", "Google", "Microsoft", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))

it_companies[0] = "VSC"
print(it_companies)

it_companies.append("Yahoo")
it_companies.insert(4, "Gmail")
it_companies[2] = it_companies[2].upper()
print(it_companies)

string_1 = "#".join(it_companies)
print(string_1)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True) 
print(it_companies)

del it_companies[0]
print(it_companies)

del it_companies[4]
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

#LEVEL 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

suma = min(ages) + max (ages)
print(suma)

print(len(ages))

print((ages[5] + ages[6]) / 2)

print((ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8] + ages[9]) / 10)


