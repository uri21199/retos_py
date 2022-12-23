### Condicionales --> link: https://aprendeconalf.es/docencia/python/ejercicios/condicionales/

#1
edad = int(input("Edad:"))
if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")

#2
variable = "contraseña"
usuario_cont = input("Ingrese la contraseña:")

if variable == usuario_cont.lower():
    print("Son iguales")
else:
    print("No son iguales")

#3
a = int(input("Numero 1:"))
b = int(input("Numero 2:"))

if b == 0:
    print("Es un error")
else:
    print(a / b)

#4
c = int(input("Numero 3:"))

if c % 2 == 0:
    print("Es par")
else:
    print("Es impar")

#5
mayor = int(input("Edad:"))
ingresos = int(input("Ingresos:"))

if mayor > 16 and ingresos >= 1000:
    print("Debe tributar")
else:
    print("No debe tributar")

#6
nombre = input("Nombre:")
sexo = input("Sexo:")

if sexo.lower() == "hombre":
    if nombre.lower() > "n":
        print("Grupo A")
    else:
        print("Grupo B")
else:
    if nombre.lower() < "m":
        print("Grupo A")
    else:
        print("Grupo B")

#7
renta_anual = int(input("Ingrese su renta anual:"))

if renta_anual < 10000:
    print("Tipo impositivo: 5%")
elif renta_anual >= 10000 and renta_anual < 20000:
    print("Tipo impositivo: 15%")
elif renta_anual >= 20000 and renta_anual < 35000:
    print("Tipo impositivo: 20%")
elif renta_anual >= 35000 and renta_anual < 60000:
    print("Tipo impositivo: 30%")
else:
    print("Tipo impositivo: 45%")

#8
punt = float(input("Ingrese su puntuación:"))

if punt == 0:
    print(f"Su nivel es inaceptable y recibirá {punt * 2400}")
elif punt == 0.4:
    print(f"Su nivel es aceptable y recibirá {punt * 2400}")
elif punt == 0.6 or punt > 0.6:
    print(f"Su nivel es meritorio y recibirá {punt * 2400}")

#9
edad2 = int(input("Edad:"))

if edad2 <= 4:
    print("Puede entrar gratis")
elif edad2 <= 18:
    print("Debe pagar 5 euros")
else:
    print("Debe pagar 10 euros")

#10
pedido = input("Quiere una pizza vegetariana?")

if pedido.lower() == "si":
    ingrediente = input("Puede elegir un solo ingrediente extra: pimiento y tofu")
    print(f"La pizza es vegetariana y lleva {ingrediente}")
else:
    ingrediente = input("Puede elegir un solo ingrediente extra: peperoni, jamón o salmón")
    print(f"La pizza no es vegetariana y lleva {ingrediente}")
