# ---------- STRINGS ----------- #

string_1 = "Un string"
string_2 = 'Otra variable string'

print(len(string_1))
print(len(string_2))
print(string_1 + "mezclando con ", string_2)
print(string_1 + "\ncon salto de linea " + string_2)

#Formateo
nombre, apellido, edad = "Lautaro", "Bustos", 23

print("Mi nombre es {} {} y mi edad es {}".format(nombre, apellido, edad))
print("Mi nombre es %s %s y mi edad es %d" %(nombre, apellido, edad))
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")

#Desempaquetar caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

#División 
language_slice = language[1:3]
print(language_slice)

#Invertir
reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.isnumeric())
print(language.count("t"))
print(language.upper().isupper())
print(language.startswith("py"))
print(language.replace('py', 'JA'))

# ---------- EJERCICIOS ---------- #
#EJERCICIO 8
company = "Coding For All"
print(company.capitalize())
print(company.title())
print(company.swapcase())

#EJERCICIO 11
print(company.replace("Coding", "Python"))

#EJERCICIO 13
print(company.split())

#EJERCICIO 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

#EJERCICIO 31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#EJERCICIO 35
radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {area} meters square.")


