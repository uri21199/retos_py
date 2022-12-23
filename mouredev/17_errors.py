# ---------- ERRORES ----------- #
#SYNTAXERROR
##print "Hola" #Descomentar para error
print("Hola")

#NAMEERROR
name = "Lautaro" #Comentar para error
print(name)

#INDEXERROR
my_list = ["Python", "JS", "GO", "CSS"]
#print(my_list[4]) --> Fuera del indice
print(my_list[3])

#MODULENOTFOUNDERROR
#import maths --> el modulo no existe
import math

#ATTRIBUTEERROR
#print(math.PI) --> el PI no existe en math
print(math.pi)

#KEYERROR
my_dict = {
    "nombre": "Lautaro",
    "apellido": "Bustos"
}
#print(my_dict["apelido"]) --> la clave apelido no existe
print(my_dict["nombre"])

#TYPEERROR
#print(my_list["nombre"]) --> los indices tiene que ser int o slices
print(my_list[2])

#IMPORTERROR
#from math import sqrts --> mal importado
from math import sqrt

#VALUEERROR
#my_int = int("10 Años")
my_int = int("10")
print(type(my_int))

#ZERODIVISIONERROR --> no se puede dividir por 0
#print(4 / 0)
print(4 / 2)




# ---------- EJERCICIOS ----------- #





