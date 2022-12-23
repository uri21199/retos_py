### Cadenas --> link: https://aprendeconalf.es/docencia/python/ejercicios/cadenas/

#1
nombre = input("Nombre:")
numero = int(input("Numero:"))

for i in range(numero):
    print(nombre)

#2
nombre_completo = input("Nombre completo:")

print(nombre_completo.lower())
print(nombre_completo.upper())
print(nombre_completo.capitalize())

#3
nombre2 = input("Nombre:")
print(f"{nombre2.upper()} tiene {len(nombre2)} letras.")

#4
tel = input("Numero de telefono:")

print(tel [4:-3])

#5
frase = input("Frase:")
print(frase[::-1])

#6
frase2 = input("Frase 2:")
vocal = input("Vocal:")

print(frase2.replace(vocal, vocal.upper()))

#7
correo = input("Correo:")
print(correo[:correo.find('@')] + '@ceu.es')

#8
precio = input("Precio:")
print(precio[:precio.find(".")], " euros y ", precio[precio.find(".") + 1:], "centimos")

#9
fecha = input("Ingrese una fecha con del formato dd/mm/yyyy:")

print(fecha[:2], "Dia")
print(fecha[3:5], "Mes")
print(fecha[6:], "Año")

#10
cesta = input("Compra:")

for i in cesta.split(","):
    print(i)

#11
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))