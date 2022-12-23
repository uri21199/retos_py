# ---------- EXCEPCIONES ----------- #
a = 5
b = 1

print(a + b)

b = "1"

try: #La prueba
    print(a + b)
    print("No hay error")
except: #Excepciones
    print("Hay un error")
else: #Si ejecuta si no hay excepción
    print("La ejecucion continua como si nada") 
finally: #Siempre
    print("La ejecucion finaliza") 

#Excepciones por tipo
try:
    print(a + b)
    print("No hay errores")
except TypeError: #Solo si hay un error de esta condición
    print("Hay un TypeError")
except ValueError: #Solo si hay un error de esta condición
    print("Hay un ValueError")

#Captura de la información de la excepción
try:
    print(a + b)
    print("No hay errores")
except ValueError as error: #Solo si hay un error de esta condición
    print(error)






# ---------- EJERCICIOS ----------- #





