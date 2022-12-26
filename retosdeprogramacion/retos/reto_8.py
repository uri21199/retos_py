# Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def aDecimal(numeroBin):
    numeroBin = str(numeroBin)
    decimal = 0
    exp = len (numeroBin) -1
    #print(decimal)
    #print(exp)
    #print(numeroBin)
    for i in numeroBin:
        decimal += (int(i) * 2**(exp))
        exp = exp - 1
        #print(decimal)
        #print(exp)
        #print(numeroBin)
    return decimal

print(aDecimal(1010011010))
