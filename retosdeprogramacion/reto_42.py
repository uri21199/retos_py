# Crea una función que transforme grados Celsius en Fahrenheit y viceversa. - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F"). - En caso contrario retornará un error. - ¿Quieres emplear lo aprendido en este reto? Revisa el reto mensual y crea una App:    https://retosdeprogramacion.com/mensuales2022/

def celfah (temp_dada):
    temp_sep = list(temp_dada.split(" "))
    print(temp_sep)
    convertido = 0

    if temp_sep[1] == "°":
        if temp_sep[2] == "C":
            convertido = convertido + int(temp_sep[0]) * 1.8 + 32
        if temp_sep[2] == "F":
            convertido += (int(temp_sep[0]) - 32) * (5/9)

    return convertido

print(celfah("50 ° F"))