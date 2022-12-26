# Crea una función que analice una matriz 3x3 compuesta por "X" y "O"y retorne lo siguiente: -"X" si han ganado las "X"  -"O" si han ganado los "O" -"Empate" si ha habido un empate-"Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. 0 si han ganado los 2.Nota: La matriz puede no estar totalmente cubierta.Se podría representar con un vacío "", por ejemplo.

def tateti(matriz):
    tablero = []
    valores = list(matriz.split(" "))

    if len(valores) <= 9:
        for i in valores:
            tablero.append(i)

        if tablero[0] == tablero[1] == tablero[2] == "X" or tablero[3] == tablero[4] == tablero[5] == "X" or tablero[6] == tablero[7] == tablero[8] == "X" or tablero[0] == tablero[4] == tablero[8] == "X" or tablero[0] == tablero[3] == tablero[6] == "X" or tablero[1] == tablero[4] == tablero[7] == "X" or tablero[2] == tablero[5] == tablero[8] == "X":
            return "X"
        elif tablero[0] == tablero[1] == tablero[2] == "O" or tablero[3] == tablero[4] == tablero[5] == "O" or tablero[6] == tablero[7] == tablero[8] == "O" or tablero[0] == tablero[4] == tablero[8] == "O" or tablero[0] == tablero[3] == tablero[6] == "O" or tablero[1] == tablero[4] == tablero[7] == "O" or tablero[2] == tablero[5] == tablero[8] == "O":
            return "O"     

    else:
        return "La extensión es mayor a la permitida (9)"


print(tateti("O O O X O X X O O"))