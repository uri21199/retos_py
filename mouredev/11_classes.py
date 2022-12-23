# ---------- CLASES ----------- #
class MyPerson:
    pass

print(MyPerson())

class Person:
    def __init__(self, name, username, alias = "Sin alias"):
        self.fullname = f"{name} {username} {alias}"
    
    def walk(self):
        print(f"{self.fullname} esta caminando")

my_person = Person("Lautaro", "Bustos")

print(my_person.fullname)
my_person.walk()

person2 = Person("Pepe", "Argento", "Guille")
print(person2.fullname)
person2.walk()





# ---------- EJERCICIOS ----------- #






