# Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas. - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy". - La función recibirá dos String y retornará un Int. - La diferencia en días será absoluta (no importa el orden de las fechas). - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

from datetime import datetime

def dif_fechas(fecha1, fecha2):
    primera = datetime.strptime(fecha1, '%d/%m/%Y')
    segunda = datetime.strptime(fecha2, '%d/%m/%Y')
    diferencia = segunda - primera
    print(abs(diferencia.days))

dif_fechas("02/11/1999", "11/09/2001")
