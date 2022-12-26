# Crea un función, que dado un año, indique el elemento y animal correspondiente en el ciclo sexagenario del zodíaco chino.- Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm - El ciclo sexagenario se corresponde con la combinación de los elementos madera, fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo (en este orden).- Cada elemento se repite dos años seguidos.- El último ciclo sexagenario comenzó en 1984 (Madera Rata).

def chino(anio : int):
    elementos = ["madera", "fuego", "tierra", "metal", "agua"]
    animales = ["rata", "buey", "tigre", "conejo", "dragon", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo"]

    if anio < 604:
        return "el ciclo sexagenario comenzó en el año 604"
    
    chino_anio = (anio - 4) % 60
    elemento_anio = elementos[round((chino_anio % 10) / 2)]
    animal_anio = animales[round(chino_anio % 12)]

    return f"{anio} {elemento_anio} {animal_anio}"

print(chino(1940))