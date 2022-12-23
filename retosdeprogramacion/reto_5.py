#Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url. - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png - Por ratio hacemos referencia por ejemplo a los "16:9" de una   imagen de 1920*1080px.

img = input("Ingrese las dimensiones de la imagen (Ej: 1920*1080):")

def ratio(imagen = img):
    imagen = img.split("*")
    uno = imagen[0]
    dos = imagen[1]
    ratio = int(uno) / int(dos)
    return f"El ratio de la imagen con dimensiones {img} es {ratio}"

print(ratio())