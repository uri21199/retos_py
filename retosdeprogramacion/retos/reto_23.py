# Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros. - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def mcd (num1, num2):
    rest = 0
    while(num2 > 0):
        rest = num2
        num2 = num1 % num2
        num1 = rest
    return num1

def mcm (num1,num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while (greater % num1 != 0) or (greater % num2 != 0):
        greater += 1
    return greater

print(mcd(2,3), mcm(4,5))