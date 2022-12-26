# Crea un programa que determine si dos vectores son ortogonales. - Los dos array deben tener la misma longitud. - Cada vector se podría representar como un array. Ejemplo: [1, -2]

def ortogonales(vec1 : list, vec2 : list):
    contador = 0
    vec2 = vec2
    for i in range(len(vec1)):
        suma = vec1[i] * vec2[i]
        contador += suma

    if contador == 0:
        return "Son ortogonales"
    else:
        return "No lo son"

print(ortogonales([4, -2, 1], [1, 3, 2]))
