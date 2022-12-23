# ---------- CONDICIONALES ----------- #

condition1 = True

if condition1:
    print("Se ejecuta la condición del if")

print("La EJECUCION continúa")

condition2 = 5 * 2

if condition2 <=  10:
    print("Se ejecuta la condición del if")

print("La EJECUCION 2 continúa")

condition3 = 11

if condition3 <= 10 and condition2 == 10 :
    print("Es menor o igual que 10")
elif condition3 == 11:
    print("Es 11")
else:
    print("Es mayor que 10")



# ---------- EJERCICIOS ----------- #
#LEVEL 1
age_user = int(input("Ingresa tu edad:"))
my_age = 23

if age_user >= 18:
    print("Estás en condiciones de manejar.")
else:
    print(f"Deberás esperar {abs(age_user - 18)} año/s para maneja.")


if age_user > my_age:
    if abs(age_user - my_age) > 1:
        print(f"Eres mayor que yo por {abs(age_user - my_age)} años.")
    else:
        print("Eres mayor que yo por 1 año.")
elif age_user == my_age:
    print("Tenemos la misma edad.")
else: 
    if abs(my_age - age_user) > 1:
        print(f"Soy mayor que vos por {abs(age_user - my_age)} años.")
    else:
        print("Soy mayor que vos por 1 año.")


number_a = int(input("Numero 1:"))
number_b = int(input("Numero 2:"))

if number_a == number_b:
    print("Son iguales")
elif number_a > number_b:
    print("A es mayor que B")
else:
    print("B es mayor que A")

#LEVEL 2
#Ej 1
scores = int(input("Ingresa tu nota:"))

if scores < 50:
    print("Tu nota es F")
elif scores >= 50 and scores < 60:
    print("Tu nota es D")
elif scores >= 60 and scores < 70:
    print("Tu nota es C")
elif scores >= 70 and scores < 90:
    print("Tu nota es B")
elif scores >= 90 and scores <= 100:
    print("Tu nota es A")

#Ej 2
season = input("Ingresa el mes:")
season = season.capitalize()
if season == "Enero" or season == "Febrero" or season == "Marzo":
    print("Estamos en otoño")
elif season == "Abril" or season == "Mayo" or season == "Junio":
    print("Estamos en verano")
elif season == "Julio" or season == "Agosto" or season == "Septiembre":
    print("Estamos en invierno")
elif season == "Octubre" or season == "Noviembre" or season == "Diciembre":
    print("Estamos en primavera")

#Ej 3
fruits = ['banana', 'orange', 'mango', 'lemon']
verdu = input("Agrega tu fruta favorita:")
verdu = verdu.lower()

if verdu in fruits:
    print("La fruta ya existe en la lista")
else:
    fruits.append(verdu)
    print(fruits)




