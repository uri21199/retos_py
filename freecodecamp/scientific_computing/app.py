class Animal:
    def __init__(self, especie, color, edad):
        self.especie = especie
        self.color = color
        self.edad = edad

    def presentar(self):
        print(f"Hola soy {self.especie} de color {self.color} y de tantos años {self.edad}")

a1 = Animal("rata", "rojo", 22)
a1.presentar()