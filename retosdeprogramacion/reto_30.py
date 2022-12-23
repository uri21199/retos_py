# Crea una función que reciba un texto y muestre cada palabra en una línea, formando un marco rectangular de asteriscos.¿Qué te parece el reto? Se vería así:
""""
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
"""

def rectangulo(texto):
    palabras = texto.split(" ")
    print("*" * 10)
    for i in palabras:
        print("* " + i + " *")
    print("*" * 10)

rectangulo("Hola como estas")
