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

    tipos_pokemon = {
        "Agua" : 1,
        "Fuego": 2,
        "Planta": 3,
        "Electrico": 4
    }
