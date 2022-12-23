### Tipos de datos --> link: https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

#1
print("Hola mundo")

#2
variable = "Hola mundo!"
print(variable)

#3
nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}")

#4
print(((3 + 2) / (2 * 5)) ** 2)

#5
horas_trabajadas = int(input("¿Cuantas horas trabaja?"))
costo = int(input("Costo por hora:"))

print(f"Trabajando {horas_trabajadas} a precio de {costo} por hora, su sueldo seria de {horas_trabajadas * costo}")

#6
entero = int(input("Ingrese su número:"))
suma = 0
for i in range(entero + 1):
    suma = suma + i
print(suma)

#7
peso = input("Ingrese su peso(en kg):")
estatura = input("Ingrese su altura (en m):")
IMC = round(int(peso) / int(estatura) ** 2, 2)

print(f"Su IMC es {IMC}")

#8
n = int(input("Numero 1:"))
m = int(input("Numero 2:"))

print(f"La división entre {n} y {m} da como cociente {n / m} y de resto {n % m}")

#9
capital = int(input("Capital:"))
interes = int(input("Interes anual:"))
anios = int(input("Años a invertir:"))
capital_obtenido = capital * interes * anios

print(f"Invirtiendo {capital} con un interés de {interes} anual e invirtiendo {anios} años, se obtendrá {capital_obtenido}")

#10
peso_payaso = 112
peso_muñeca = 75
payasos_pedido = int(input("Payasos:"))
muñecas_pedido = int(input("muñecas:"))
peso_total = payasos_pedido * peso_payaso + muñecas_pedido * peso_muñeca
print(f"El peso total es {peso_total}")

#11
interes = 4
dinero = int(input("Dinero:"))
primero = dinero * interes
segundo = dinero * (interes * 2)
tercero = dinero * (interes * 3)

print(f"{primero}, {segundo}, {tercero}")

#12
pan = 3.49
no_dia = pan - (pan * 0.6)
venta = int(input("Pan:"))

print(f"{pan * venta}, {pan * venta - no_dia * venta}, {no_dia * venta}")