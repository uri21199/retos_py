#Crea una función que reciba dos cadenas como parámetro (str1, str2) imprima otras dos cadenas como salida (out1, out2). out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2. out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

def salidas(cad1, cad2):
    out1 = ""
    out2 = ""

    for i in cad1:
        if i not in cad2:
            out1 = out1 + i

    for i in cad2:
        if i not in cad1:
            out2 = out2 + i
    
    print(f"La cadena resultante 1 es '{out1}' y la cadena resultante 2 es'{out2}'")

salidas("Perro", "Geto")