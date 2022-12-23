### Ficheros --> Link: https://aprendeconalf.es/docencia/python/ejercicios/ficheros/

#1: Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

print("1")

n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
f = open(nombre_fichero, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()

#2: Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

print("\n2")

n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try: 
    f = open(nombre_fichero, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())
    f.close()

#3: Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

print("\n3")

n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try: 
    with open(nombre_fichero, 'r') as f:
        lineas = f.readlines()
    print(lineas[m - 1])
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)

#4: Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.

print("\n4")

def contar_palabras(url):
    from urllib import request
    from urllib.error import URLError
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = f.read()
        return len(contenido.split())

print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras('https://no-existe.txt'))

#5: Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.

print("\n5")

def parsear_pib(url):
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(url) as f:
            datos = f.read().decode('utf-8').split('\n') # Leer los datos y guardar cada línea en una lista.
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        años = datos.pop(0).split('\t')[1:]        # Obtenemos los años de la primera linea del fichero.
        dict_pibs = {}              # Creamos el diccionario prinpipal para guardar los pibs de todos los países.
        for pais in datos:        # Bucle iterativo para recorrer las líneas del fichero.
            datos_pais = pais.split('\t')  # Obtenemos el código del país de los dos últimos caracteres del primer campo de la linea.
            codigo_pais = datos_pais.pop(0)[-2:]  # Construimos un diccionario con los años y el pib del pais.
            dict_pais = {}
            for i in range(len(datos_pais)): # Bucle iterativo para recorrer los pibs del país.
                dict_pais[años[i].strip()] = datos_pais[i].strip() # Añadimos el diccionario con los pib del país al diccionario principal
            dict_pibs[codigo_pais] = dict_pais
        return dict_pibs

def pib(pibs, pais = "ES"):
    print("Año\tPIB")
    for i, j in pibs[pais].items():
        print(i, '\t', j)

pais = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', pais)
pib(parsear_pib("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"), pais)

#6: Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

print("\n6")

def get_phone(file, client):
    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if client in directory:
            return directory[client]
        else:
            return('¡El cliente ' + client + ' no existe!\n')


def add_phone(file, client, telf):
    try: 
        f = open(file, 'a')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        f.write(client + ',' + telf + '\n')
        f.close()
        return('El teléfono se ha añadido.\n')

def remove_phone(file, client):
    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if client in directory:
            del directory[client]
            f = open(file, 'w')
            for name, telf in directory.items():
                f.write(name + ',' + telf)
            f.close()
            return ('¡El cliente se ha borrado!\n')
        else:
            return('¡El cliente ' + client + ' no existe!\n')

def create_directory(file):
    import os
    if os.path.isfile(file):
        answer = input('El fichero ' + file + ' ya existe. ¿Desea vaciarlo (S/N)? ')
        if answer == 'N': 
            return 'No se ha creado el fichero porque ya existe.\n'
    f = open(file, 'w')
    f.close()
    return 'Se ha creado el fichero.\n'

def menu():
    print('Gesión del listín telefónico')
    print('============================')
    print('1 - Consultar un teléfono')
    print('2 - Añadir un teléfono')
    print('3 - Eliminar un teléfono')
    print('4 - Crear el listín')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option


def directory():
    file = 'listin.txt' 
    while True:
        option = menu()
        if option == '1':
            name = input('Introduce el nombre del cliente: ')
            print(get_phone(file, name))
        elif option == '2':
            name = input('Introduce el nombre del cliente: ')
            telf = input('Introduce el teléfono del cliente: ')
            print(add_phone(file, name, telf))
        elif option == '3':
            name = input('Introduce el nombre del cliente: ')
            print(remove_phone(file, name))
        elif option == '4':
            print(create_directory(file))
        else:
            break
    return

directory()

#7:El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas. Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna.

print("\n7")

def limpiar(cifra):
    cifra = cifra.replace('.', '')
    cifra = cifra.replace(',','.')
    return float(cifra) 

def preprocesado(ruta):
    try:
        # Abrimos el fichero en modo lectura
        with open(ruta, 'r') as f:
            # Leemos el fichero por líneas en una lista
            lineas = f.read().split('\n')
    except FileNotFoundError:
        print('El fichero no existe.')
        return
    # Leemos las claves del primer elemento de la lista y creamos una lista dividiendo la línea por el punto y coma.
    claves = lineas.pop(0).split(";")
    # Creamos el diccionario para guardar las cotizaciones
    cotizaciones = {}
    # Inicializamos el diccionario con listas vacías
    for i in claves:
        cotizaciones[i] = []
    # Bucle iterativo para recorrer la lista de lineas
    for linea in lineas:
        # Creamos una lista con los campos dividiendo la línea por el punto y coma
        campos = linea.split(';')
        # Añadimos el primer campo (el nombre de la empresa) a la lista del diccionario
        cotizaciones[claves[0]].append(campos[0])
        # Bucle iterativo para añadir el resto de los campos a las listas correspondientes del diccionario. 
        # Previamente los campos se limpian del carácter de separación de miles y se sustituye la coma por el punto para el separador de decimales.
        for i in range(1, len(campos)):
            cotizaciones[claves[i]].append(limpiar(campos[i]))
    return cotizaciones


def resumen_cotizacion(cotizaciones, ruta):
    # Eliminamos el primer par del diccionario que contiene los nombres de las empresas.
    del(cotizaciones['Nombre']) # Inicializamos una cadena con el contenido que después se escribirá en el fichero.
    contenido = ""  # Escribimos en la primera línea los nombres de las columnas.
    contenido += 'Nombre'   # Bucle iterativo para crear los encabezados de las cotizaciones.
    for i in cotizaciones:
        contenido += ";" + i    # Calculamos los mínimos de cada lista y los escribimos en las columnas correspondientes
    contenido += '\nMínimo'
    for i in cotizaciones.values():
        contenido += ';' + str(min(i))
    contenido += '\nMáximo'     # Calculamos los máximos de cada lista y los escribimos en las columnas correspondientes
    for i in cotizaciones.values():
        contenido += ';' + str(max(i))
    contenido += '\nMedia'     # Calculamos las medias de cada lista y las escribimos en las columnas correspondientes
    for i in cotizaciones.values():
        contenido += ';' + str(sum(i)/len(i))
    with open(ruta, 'w') as f:     # Abrimos el fichero en modo escritura.
        f.write(contenido)         # Escribimos el contenido en el fichero
    return


# Llamada a las funciones de prueba
cotizaciones = preprocesado('cotizacion.csv')
print(cotizaciones)
resumen_cotizacion(cotizaciones, 'resumen-cotizacion.csv')

#8: El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones: Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos. Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%. Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.

print("\n8")

def nota(cifra):
    cifra = cifra.replace(',','.')
    return float(cifra) 

def calificaciones(ruta):
    try:
        # Abrimos el fichero en modo lectura
        f = open(ruta, 'r')
    except FileNotFoundError:
        print('El fichero no existe.')
        return
    # Leemos el fichero por líneas en una lista
    lineas = f.readlines()
    # Cerramos el fichero
    f.close()
    # Leemos las claves del primer elemento de la lista, eliminamos el cambio de línea que aparece al final y dividimos la cadena por el punto y coma.
    claves = lineas[0][:-1].split(";")
    # Creamos la lista de calificaciones
    calificaciones = []
    # Recorremos las líneas del fichero y para cada línea creamos un diccionario que añadimos a la lista de calificaciones.
    for i in lineas[1:]:
        # Eliminamos el cambio de línea del final y dividimos la cadena por el punto y coma.
        valores = i[:-1].split(";")
        # Creamos un diccionario vacío para ir añadiendo los datos de cada alumno.
        alumno = {}
        # Recorremos la lista de valores y los añadimos al diccionario.
        for j in range(len(valores)):
            alumno[claves[j]] = valores[j]
        # Añadimos el diccionario a la lista de calificaciones
        calificaciones.append(alumno)
    return calificaciones

def añadir_nota_final(calificaciones):

    def nota_final(alumno):
        if alumno['Ordinario1']: #Si el alumno se ha presentado al examen de repesca del primer parcial tomamos esa nota como la nota del primer parcial
            parcial1 = nota(alumno['Ordinario1'])
        elif alumno['Parcial1']:
            parcial1 = nota(alumno['Parcial1'])
        else: # No se ha presentado al primer parcial ni a la repesca en el ordinario
            parcial1 = 0
        if alumno['Ordinario2']: #Si el alumno se ha presentado al examen de repesca del segundo parcial tomamos esa nota como la nota del segundo parcial
            parcial2 = nota(alumno['Ordinario2'])
        elif alumno['Parcial2']:
            parcial2 = nota(alumno['Parcial2'])
        else: # No se ha presentado al segundo parcial ni a la repesca en el ordinario
            parcial2 = 0 
        if alumno['OrdinarioPracticas']: #Si el alumno se ha presentado al examen de repesca de prácticas tomamos esa nota como la nota de prácticas
            practicas = nota(alumno['OrdinarioPracticas'])
        elif alumno['Practicas']:
            practicas = nota(alumno['Practicas'])
        else:
            practicas = 0
        alumno['Final1'] = parcial1
        alumno['Final2'] = parcial2
        alumno['FinalPracticas'] = practicas
        alumno['NotaFinal'] = parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4
        return alumno

    # Aplicamos la función nota_final a todos los alumnos
    return list(map(nota_final, calificaciones))

def aprobados_suspensos(calificaciones):
    # Creamos las listas de aprobados y suspensos vacías
    aprobados = []
    suspensos = []
    # Recorremos los alumnos del curso
    for alumno in calificaciones:
        # Si se cumplen las condiciones para aprobar añadimos el nombre del alumno a la lista de aprobados y si no a la de suspensos.
        if all([int(alumno['Asistencia'][:-1]) >= 75, alumno['Final1'] >= 4, alumno['Final2'] >=4, alumno['FinalPracticas'] >=4, alumno['NotaFinal'] >= 5]):
            aprobados.append(alumno['Apellidos'] + ', ' + alumno['Nombre'])
        else:
            suspensos.append(alumno['Apellidos'] + ', ' + alumno['Nombre'])
    return aprobados, suspensos

# Llamada a las funciones de prueba
print(añadir_nota_final(calificaciones('calificaciones.csv')))
aprobados, suspensos = aprobados_suspensos(añadir_nota_final(calificaciones('calificaciones.csv')))
print('Lista de aprobados:', aprobados)
print('Lista de suspensos:', suspensos)
