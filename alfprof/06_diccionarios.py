### Diccionarios --> link: https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/

#1
print("1")

divisas =  {
'Euro':'€', 
'Dollar':'$', 
'Yen':'¥'}

divisa_user = input("Ingrese la divisa:")
print(divisas[divisa_user])

#2
print("\n2")

datos = {
    "Nombre": input("Ingrese su nombre:"),
    "Edad": input("Ingrese su edad:"),
    "Dirección": input("Ingrese su dirección:")
}

print(f"{datos['Nombre']} tiene {datos['Edad']} años y vive en {datos['Dirección']}")

#3
print("\n3")

frutas = {
    "Plátano": 1.35,
    "Manzana": 0.8,
    "Pera": 0.85,
    "Naranja": 0.7
}

fruta = input("Fruta:").capitalize()
kg = input("Kilos:")

if fruta.title() in frutas:
    print(f"Pidió {kg} kg de {fruta}. El gasto total es de {round(frutas[fruta] * float(kg), 2)}")
else:
    print(f"La fruta {fruta} no está.")

#4
print("\n4")

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

fecha = input("Fecha en formato dd/mm/yyyy:")
fecha = fecha.split("/")
print(f"El dia numero {fecha[0]} del mes {meses[int(fecha[1])]} del año {fecha[2]}")

#5
print("\n5")

materias = {
    "Matemáticas": 6,
    "Física": 4,
    "Química": 5
}
creditos_totales = 0

for i in materias:
    print(f"{i} tiene {materias[i]} créditos.")
    creditos_totales = creditos_totales + materias[i]

print(f"Hay {creditos_totales} créditos totales.")

#6
print("\n6")

persona = {}
continuar = True
while continuar:
    clave = input("Que dato quieres introducir?")
    valor = input(f"{clave}:")
    persona[clave] = valor
    print(persona)
    continuar = input("Quieres seguir agregando? (Si/No)").lower() == "si"

#7
print("\n7")

compra = {}
continuar = True
while continuar:
    clave = input("Que compraste?")
    precio = input(f"Precio de {clave}:")
    compra[clave] = float(precio)
    print(compra)
    continuar = input("Quieres seguir agregando? (Si/No)").lower() == "si"

gasto = 0
print("Lista:")
for item, precio in compra.items():
    print(f"{item}: {precio}")
    gasto += float(precio)
print(f"Gasto total: {gasto}")

#8
print("\n8")

diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')


#9
print("\n9")

facturas = {}
cobrado = 0
pendiente = 0
more = ''
while more != 'T':
    if more == 'A':
        clave = input('Introduce el número de la factura: ')
        coste = float(input('Introduce el coste de la factura: '))
        facturas[clave] = coste
        pendiente += coste
    if more == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste
    print('Recaudado:', cobrado)
    print('Pendiente de cobro: ', pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')

#10
print("\n10")

clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        telefono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
        clientes[nif] = cliente
    if opcion == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')


#11
print("\n11")

# Cadena con los datos de los clientes de la empresa
datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# Dividimos la cadena por el caracter de cambio de línea \n y creamos una lista con las subcadenas
lista_clientes = datos_clientes.split('\n')
# Inicializamos el diccionario que va a contener el directorio de clientes a vacío.
directorio = {}
# Dividimos la cadena del primer elemento de la lista de clientes (que contienen los 
# nombres de los campos) por el caracter ; y creamos una lista con los campos.
lista_campos = lista_clientes[0].split(';') 
# Bucle iterativo para recorrer los elementos de la lista lista_clientes.
# la variable cliente recorre desde el segundo elemento hasta el último elemento de la lista 
# (el primer elemento contiene los nombres de campo así que no corresponde a un cliente)
for i in lista_clientes[1:]:
    # Inicializamos el diccionario que va a contener los datos del cliente actual a vacío.
    cliente = {}
    # Dividimos la cadena i por el caracter ; y creamos una lista con las subcadenas con la
    # información del cliente
    lista_info = i.split(';') 
    # Bucle iterativo para recorrer los campos y añadir los pares al diccionario del cliente.
    # j toma valores de 1 al número de campos menos 1. El primer elemento (posición 0) corresponde 
    # al nif y no se añade al diccionario porque se utilizará después como clave en el diccionario
    # principal
    for j in range(1,len(lista_campos)):
        # Condicional. Si el campo actual es descuento convertimos su valor en real
        if lista_campos[j] == 'descuento':
            lista_info[j] = float(lista_info[j])
        cliente[lista_campos[j]] = lista_info[j]
    # Añadirmos un par al diccionario del directorio con la clave el nif del cliente y valor
    # el diccionario que acabamos de crear con el resto de sus datos.
    directorio[lista_info[0]] = cliente
# Mostramos el diccionario por pantalla
print(directorio)
