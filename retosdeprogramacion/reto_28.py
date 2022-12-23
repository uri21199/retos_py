# Simula el funcionamiento de una máquina expendedora creando una operaciónque reciba dinero (array de monedas) y un número que indique la selección del producto. - El programa retornará el nombre del producto y un array con el dinero  de vuelta (con el menor número de monedas).- Si el dinero es insuficiente o el número de producto no existe,  deberá indicarse con un mensaje y retornar todas las monedas. - Si no hay dinero de vuelta, el array se retornará vacío.- Para que resulte más simple, trabajaremos en céntimos con monedas  de 5, 10, 50, 100 y 200.- Debemos controlar que las monedas enviadas estén dentro de las soportadas.

def maquina(dinero, nro_prod):

    productos = {
        1 : 100,
        2 : 200,
        3 : 75,
        4 : 124
    }

    elegido = productos.get(nro_prod)

    din_ingresado = []

    for i in range(len(dinero)):
        if dinero[i] != 5 and dinero[i] != 10 and dinero[i] != 50 and dinero[i] != 100 and dinero[i] != 200:
            return "Alguna/s de las monedas ingresadas no es/son reconocida/s por la máquina expendedora. \nSolo se puede ingresar monedas de 5, 10, 50, 100 o 200."
            break
        else:
            din_ingresado.append(dinero[i])

    if len(din_ingresado) == len(dinero):
        dinero_total = 0
        for i in range(len(din_ingresado)):
            dinero_total += din_ingresado[i]
        
        vuelto = dinero_total - elegido

        return f"Usted ingreso ${dinero_total} para comprar el producto n° {nro_prod} que cuesta {elegido}. Su vuelto es de {vuelto}"

print(maquina([5, 10,50,100,200], 4))
