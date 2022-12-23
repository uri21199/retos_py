#Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas. - Los signos de puntuación no forman parte de la palabra. - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas. - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

def contar_palabras(cadena):
    palabras = cadena.split(" ")
    print (palabras)
    for i in palabras:
        print(i)
        for j in palabras:
            if j == i:
                print(j)

contar_palabras("perro tigre hola")