# Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.

def miliseg (dia : int, hora : int, mins : int, seg : int):
    cantidad = dia * 24 * 60 * 60 * 1000 + hora * 60 * 60 * 1000 + mins * 60 * 1000 + seg * 1000 
    return cantidad

print(miliseg(10, 3, 13, 20))