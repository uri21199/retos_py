# ---------- TUPLES ----------- #
my_t = tuple() #No deja cambiar/agregar los elementos 
my_tuple = (23, "Lautaro", 23)
print(my_tuple)
print(my_tuple.count(23))
print(my_tuple.index(23))



# ---------- EJERCICIOS ----------- #
#LEVEL 1
tup = tuple()
brothers = ("Jona", "Juan", "Hector", "Cruz")
sisters = ("Tama", "Soledad", "Abril", "Ainara")

siblings = brothers + sisters
print(siblings)
print(len(siblings))

siblings = list(siblings)
siblings.append("Norma")
siblings.append("Beatriz")
print(siblings)

family_members = tuple(siblings)
print(family_members)