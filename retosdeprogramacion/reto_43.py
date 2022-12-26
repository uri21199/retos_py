# Este es un reto especial por Halloween. Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato" y un listado (array) de personas con las siguientes propiedades:
# - Nombre de la niña o niño
# - Edad
# - Altura en centímetros
#Si las personas han pedido trato, el programa retornará dulces (aleatorios) siguiendo estos criterios:
#- Un dulce por cada letra de nombre
#- Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
#- Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
#- Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
# Si las personas han pedido truco, el programa retornará sustos (aleatorios) siguiendo estos criterios:
#- Un susto por cada 2 letras del nombre por persona
#- Dos sustos por cada edad que sea un número par
#- Tres sustos por cada 100 cm de altura entre todas las personas
#- Sustos: 🎃 👻 💀 🕷 🕸 🦇

import random

def halloween(opc, listado):
    #Truco
    sustos = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
    if opc == "Truco":
        sustos_totales = ""
        cantidad_sustos = 0
        for a in range(len(listado)):
            #Nombre
            letras_nombre = list(listado[a]["Nombre"])
            b = 2
            while b <= len(letras_nombre):
                sustos_totales += f"{sustos[random.randint(0, 5)]} "
                cantidad_sustos += 1
                b += 2

            #Edad
            edad = listado[a]["Edad"]
            if edad % 2 == 0:
                sustos_totales += f"{sustos[random.randint(0, 5)]} "
                cantidad_sustos += 1
            
            #Altura
            altura = listado[a]["Altura"]
            alt_base = 100
            while alt_base <= altura:
                sustos_totales += f"{sustos[random.randint(0, 5)]} " * 3
                cantidad_sustos += 3
                alt_base += 100


        return f"{sustos_totales}\nEl total es de {cantidad_sustos} sustos."


    #Trato
    dulces = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]
    if opc == "Trato":
        dulces_totales = ""
        cantidad_dulces = 0
        for i in range(len(listado)):
            #Nombre
            letras_nombre = list(listado[i]["Nombre"])
            for j in range(len(letras_nombre)):
                dulces_totales += f"{dulces[random.randint(0, 7)]} "
                cantidad_dulces += 1

            #Edad
            edad = listado[i]["Edad"]
            if edad >= 10:
                dulces_totales += f"{dulces[random.randint(0, 7)]} " * 3
                cantidad_dulces += 3
            elif edad < 10:
                k = 3
                while k <= edad:
                    dulces_totales += f"{dulces[random.randint(0, 7)]} "
                    k += 3
                    cantidad_dulces += 1
        

            #Altura
            altura = listado[i]["Altura"]
            if altura >= 150:
                dulces_totales += f"{dulces[random.randint(0, 7)]} " * 6
                cantidad_dulces += 6
            elif altura < 150:
                k = 50
                while k <= edad:
                    dulces_totales += f"{dulces[random.randint(0, 7)]} " * 2
                    k += 50
                    cantidad_dulces += 2

        return f"{dulces_totales}\nEl total es de {cantidad_dulces} dulces."

print(halloween("Trato",[{"Nombre": "Lautaro", "Edad": 23, "Altura": 183}, {"Nombre": "Azul", "Edad": 5, "Altura": 134}]))
print(halloween("Truco",[{"Nombre": "Lautaro", "Edad": 22, "Altura": 183}, {"Nombre": "Azul", "Edad": 5, "Altura": 134}]))