# ---------- MANEJO DE PAQUETES ----------- #

#PIP
import numpy 
print(numpy.version.version)

numpy_array = numpy.array([10, 20, 30, 40, 50])
print(type(numpy_array))
print(numpy_array)

import pandas as pd
print(pd.array([10, 20, 30]))

#pip list
#pip uninstall pandas
#pip show numpy

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=15")
print(response)
print(response.status_code)
print(response.json())

from my_package import cuentas
print(cuentas.sum(2,3))

# ---------- EJERCICIOS ----------- #
#1
response2 = requests.get("https://www.gutenberg.org/files/1112/1112.txt")