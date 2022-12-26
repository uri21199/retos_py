# Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.

for i in range(1, 101):
    print(i)

print("----------")

contador = 1

while contador <= 100:
    print(contador)
    contador += 1
