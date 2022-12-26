# Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm. - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales). - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".

def ley_ohm(param1 : dict, param2 : dict):
    if "V" not in param1 and "V" not in param2:
        claves1 = list(param1)
        claves2 = list(param2)

        resultado = param1[claves1[0]] * param2[claves2[0]]
        return f"El faltante es V y el resultado es {resultado}"

    elif "R" not in param1 and "R" not in param2:
        claves1 = list(param1)
        claves2 = list(param2)

        if claves1[0] == "V":
            resultado = param1[claves1[0]] / param2[claves2[0]]
            return f"El faltante es R y el resultado es {resultado}"
        else:
            resultado = param2[claves2[0]] / param1[claves1[0]]
            return f"El faltante es R y el resultado es {resultado}"

    elif "I" not in param1 and "I" not in param2:
        claves1 = list(param1)
        claves2 = list(param2)

        if claves1[0] == "V":
            resultado = param1[claves1[0]] / param2[claves2[0]]
            return f"El faltante es I y el resultado es {resultado}"
        else:
            resultado = param2[claves2[0]] / param1[claves1[0]]
            return f"El faltante es I y el resultado es {resultado}"


print(ley_ohm({"V": 30}, {"R": 8}))
