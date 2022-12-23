# Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*". - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra. - EXTRA: ¿Eres capaz de dibujar más figuras?

def dibujar(forma, tamanio : int):
    if forma == "cuadrado":
        for i in range(tamanio):
            print("*" * tamanio)

    if forma == "triangulo":
        for i in range(1, tamanio + 1):
            print("*" * i)

dibujar("cuadrado", 3)