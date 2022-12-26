# Crea un programa que calcule quien gana más partidas al piedra, papel, tijera. - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate) - La función recibe un listado que contiene pares, representando cada jugada. - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".

def ppt(entrada):
    contador1 = 0
    contador2 = 0 

    for i in entrada:
        if i[0] == "R" and i[1] == "S":
            contador1 = contador1 + 1
        if i[0] == "R" and i[1] == "R":
            continue
        if i[0] == "R" and i[1] == "P":
            contador2 = contador2 + 1
        if i[0] == "P" and i[1] == "S":
            contador2 = contador2 + 1
        if i[0] == "P" and i[1] == "R":
            contador1 = contador1 + 1
        if i[0] == "P" and i[1] == "P":
            continue
        if i[0] == "S" and i[1] == "S":
            continue
        if i[0] == "S" and i[1] == "R":
            contador2 = contador2 + 1
        if i[0] == "S" and i[1] == "P":
            contador1 = contador1 + 1
    
    if contador1 > contador2:
        return "Gana 1"
    elif contador2 > contador1:
        return "Gana 2"
    else:
        return "Empate"

print(ppt([("R","S"), ("S","R"), ("P","S"), ("R", "S"), ("R", "S")]))
