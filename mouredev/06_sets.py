# ---------- SETS ----------- #
my_set = {"Lautaro", "Bustos", 23} #Un set no es una estructura ordenada, no admite repetidos
my_set.add("Tigre")
print(my_set)

print("Lautaro"in my_set)

my_set.remove("Tigre")
print(my_set)


my_set_2 = {"dato 1", "dato 2", 23}
sum_set = my_set.union(my_set_2)
print(sum_set)
print(my_set_2.update("dato 3", "dato 4", "dato 5"))

print(sum_set.union({"Js", "React"}))

print(sum_set.difference(my_set_2))

print(my_set.intersection(my_set_2))

my_set.clear()
print(my_set)

del my_set
# ---------- EJERCICIOS ----------- #
#LEVEL 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update({"Gmail", "Wsp", "Linkedin"})
print(it_companies)

it_companies.remove("Gmail")
print(it_companies)

#LEVEL 2
sum_ab = A.union(B)
print(sum_ab)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.symmetric_difference(B))

del A 
del B

#LEVEL 3

print(len(age) > len(set(age)))
