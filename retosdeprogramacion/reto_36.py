# La Tierra Media está en guerra! En ella lucharán razas leales a Sauron contra otras bondadosas que no quieren que el mal reine sobre sus tierras. Cada raza tiene asociado un "valor" entre 1 y 5:
#- Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
#- Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
# Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
#- El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la suma del valor del ejército y el número de integrantes.
#- Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
#- Tienes total libertad para modelar los datos del ejercicio.
#Ej: 1 Peloso pierde contra 1 Orco - 2 Pelosos empatan contra 1 Orco - 3 Pelosos ganan a 1 Orco

def tierra_media(bond, malv):

    bondadosas = {
        "Pelosos": 1,
        "Sureños buenos": 2,
        "Enanos": 3,
        "Númenóreanos": 4,
        "Elfos": 5
    }

    malvadas = {
        "Sureños malos": 2,
        "Orcos": 2,
        "Goblins": 2,
        "Huargos": 3,
        "Trolls": 5
    }

    ejercito_bondadoso = 0
    ejercito_malvado = 0

    for i in range(len(bond)):
        valor_bond = bond[i]
        ejercito_bondadoso += bondadosas[valor_bond]
    
    for i in range(len(malv)):
        valor_malv = malv[i]
        ejercito_malvado += malvadas[valor_malv]

    if ejercito_bondadoso > ejercito_malvado:
        return "Ganan los buenos"
    elif ejercito_malvado > ejercito_bondadoso:
        return "Ganan los malos"
    else:
        return "Empate"

print(tierra_media(["Elfos", "Elfos", "Pelosos"], ["Orcos", "Huargos", "Sureños malos", "Goblins", "Goblins"]))
print(tierra_media(["Elfos", "Elfos", "Pelosos"], ["Orcos", "Huargos"]))
print(tierra_media(["Elfos"], ["Orcos", "Huargos", "Sureños malos", "Goblins", "Goblins"]))