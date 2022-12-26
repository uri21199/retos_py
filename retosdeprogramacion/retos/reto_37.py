# ¡Han anunciado un nuevo "The Legend of Zelda"! Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos"The Legend of Zelda" de la historia? Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zeldaque tú selecciones. - Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)

from datetime import datetime

def dif_juegos():

    fechas_juegos = {
        "Skyward Sword": datetime(2022, 9, 3),
        "Link's Awakening": datetime(2022, 2, 23),
        "The Champions Ballad": datetime(2021, 8, 11),
        "The Masters Trial": datetime(2020, 9, 9)
    }

    fecha_tears = datetime(2023, 12, 5)

    juego_ing = input("Ingresa el juego:")

    diferencia = fecha_tears - fechas_juegos[juego_ing]

    return diferencia


print(dif_juegos())
