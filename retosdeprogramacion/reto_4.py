# Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono. - La función recibirá por parámetro sólo UN polígono a la vez. - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo. - Imprime el cálculo del área de un polígono de cada tipo.

def areas(poligono):
    if poligono.lower() == "cuadrado":
        lado = int(input("Ingrese la longitud de sus lados (en cm):"))
        area = lado * lado
        print(f"El área del cuadrado es de {area} cm2.")
    elif poligono.lower() == "rectangulo":
        altura_r = int(input("Ingrese la altura del rectángulo:"))
        base_r = int(input("Ingrese la base del rectángulo:"))
        area_r = base_r * altura_r
        print(f"El área del rectángulo es de {area_r} cm2.")
    elif poligono.lower() == "triangulo":
        altura_t = int(input("Ingrese la altura del triángulo:"))
        base_t = int(input("Ingrese la base del triángulo:"))
        area_t = (altura_t * base_t) / 2
        print(f"El area del triangulo es de {area_t} cm2.")
    else:
        print("No se puede calcular el area del poligono solicitado.")

areas("triangulo")
