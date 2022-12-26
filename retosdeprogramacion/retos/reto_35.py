# Crea un programa que calcule el daño de un ataque durante una batalla Pokémon. 
# - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad 
# - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo) 
# - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad) 
# - El programa recibe los siguientes parámetros: 
#       - Tipo del Pokémon atacante. 
#       - Tipo del Pokémon defensor. 
#       - Ataque: Entre 1 y 100. 
#       - Defensa: Entre 1 y 100.

def ataque(tipo_att, tipo_def, att, defe):
    efectividad = 0
    if tipo_att == "Agua" and tipo_def == "Fuego":
        efectividad = 2
    elif tipo_att == "Agua" and tipo_def == "Planta":
        efectividad = 0.5
    elif tipo_att == "Agua" and tipo_def == "Agua":
        efectividad = 1
    elif tipo_att == "Agua" and tipo_def == "Eléctrico":
        efectividad = 0.5
    elif tipo_att == "Planta" and tipo_def == "Fuego":
        efectividad = 0.5
    elif tipo_att == "Planta" and tipo_def == "Agua":
        efectividad = 2
    elif tipo_att == "Planta" and tipo_def == "Planta":
        efectividad = 0.5
    elif tipo_att == "Planta" and tipo_def == "Eléctrico":
        efectividad = 1
    elif tipo_att == "Fuego" and tipo_def == "Planta":
        efectividad = 2
    elif tipo_att == "Fuego" and tipo_def == "Agua":
        efectividad = 0.5
    elif tipo_att == "Fuego" and tipo_def == "Fuego":
        efectividad = 0.5
    elif tipo_att == "Fuego" and tipo_def == "Eléctrico":
        efectividad = 1
    elif tipo_att == "Eléctrico" and tipo_def == "Planta":
        efectividad = 0.5
    elif tipo_att == "Eléctrico" and tipo_def == "Agua":
        efectividad = 2
    elif tipo_att == "Eléctrico" and tipo_def == "Eléctrico":
        efectividad = 0.5
    elif tipo_att == "Eléctrico" and tipo_def == "Fuego":
        efectividad = 1

    daño = 50 * (att / defe) * efectividad 
    return daño

print(ataque("Eléctrico", "Fuego", 20, 20))
