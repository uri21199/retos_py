# Crea un programa que sea capaz de transformar texto natural a código morse y viceversa. - Debe detectar automáticamente de qué tipo se trata y realizar la conversión. - En morse se soporta raya "—", punto ".", un espacio " " entre letras   o símbolos y dos espacios entre palabras "  ". - El alfabeto morse soportado será el mostrado en   https://es.wikipedia.org/wiki/Código_morse

diccionario = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", 
    "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
}

def codigo_morse(texto):
    letras = texto.split()
    codigo = []
    for i in letras:
        for j in i:
            cod_j = diccionario[j.lower()]
            codigo.append((j, cod_j))
    print(texto)
    print(codigo)

codigo_morse("Hola tigre de bengala")
