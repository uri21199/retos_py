# ---------- EXPRESIONES REGULARES ----------- #

import re

my_string = "Esta es la lección número 7: Expresiones Regulares"
my_string2 = "Esta no es la lección número 6: Lección de Manejo de ficheros"

#match() --> busca desde el principio del str
print(re.match("Esta es la lección", my_string))
print(re.match("Esta es la lección", my_string2))

#I --> reconoce mayus, min, todo
match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_string2)
if match != None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])
    print("Se hizo el if")
else:
    print("No se pudo ejecutar porque match es None")

#search
search = re.search("lección", my_string, re.I)
print(search)
start, end = match.span()
print(my_string[start:(end - 2)])

#findall
findall = re.findall("lección", my_string2, re.I)
print(findall)

#split
print(re.split(":", my_string))

#sub
print(re.sub("Expresiones", "expresiones", my_string))
print(re.sub("expresiones regulares", "RegEx", my_string.lower(), re.I))

#patterns
pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|expresiones"
print(re.findall(pattern, my_string.lower()))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))


# ---------- EJERCICIOS ----------- #
#LEVEL 1
#1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

lista_para = paragraph.split()

cantidad = []
for i in lista_para:
    elemento = (len(re.findall(i, paragraph)), i)
    print(elemento)
    cantidad.append(elemento)
print(cantidad)

#2
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]