# Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista). Si no conoces qué es un número de Armstrong, debes buscar información  al respecto.

def armstrong(numero):
    pot = len(str(numero))
    ind = list(str(numero))
    entero = int(numero)
    contador = 0

    for i in ind:
        contador += int(i) ** int(pot)
    
    if contador == entero:
        return True
    else:
        return False

print(armstrong(1634))
