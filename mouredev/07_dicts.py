# ---------- DICCIONARIOS ----------- #
my_dict = dict()

dict_two = {
    "nombre": "Lautaro",
    "apellido": "Bustos",
    "edad" : 23,
    "lenguajes" : {"Python", "Javascript", "React"}
}

print(dict_two)
print(dict_two["apellido"])

dict_two["nombre"] = "Uriel"
print(dict_two["nombre"])

dict_two["color"] = "Azul"
print(dict_two)

del dict_two["color"]
print(dict_two)

print("Uriel" in dict_two)
print("apellido" in dict_two)

print(dict_two.items())
print(dict_two.keys())
print(dict_two.values())

new_dict = dict.fromkeys(("Nombre", "Apellido", "Direccion"))
print(new_dict)

dict_two.pop("nombre")
print(dict_two)

dict_two.popitem()
print(dict_two)

# ---------- EJERCICIOS ----------- #
dog = dict()
dog["name"] = "Firu"
dog["color"] = "Blanco"
dog["legs"] = 4
dog["age"] = 10

print(dog)

student = {
    "nombre": "Lautaro",
    "apellido": "Bustos", 
    "edad": 23,
    "sexo": "masculino",
    "estado civil": "soltero",
    "habilidades": {"programar", "correr", "estudiar"},
    "pais": "Argentina",
    "ciudad": "buenos aires", 
    "direccion": "peron 689"
}

print(len(student))
print(student.values())
print(list(student.keys()))
print(list(student.values()))
student.pop("estado civil")
print(student)
del dog
print(dog)
