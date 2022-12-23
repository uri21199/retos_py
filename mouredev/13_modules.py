# ---------- MODULOS ----------- #
from module import sum 

sum(2, 2)

import module
module.resta(2, 2)

from math import sqrt
print(sqrt(9))

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(round(mean(ages), 2))       # ~22.9
print(round(median(ages), 2))     # 23
print(round(mode(ages), 2))       # 20
print(round(stdev(ages), 2))      # ~2.3



# ---------- EJERCICIOS ----------- #
#LEVEL 1
#1
from random import random
def random_user_id():
    car1 = random()
    car2 = random()
    car3 = random()
    car4 = random()
    car5 = random()
    car6 = random()
    print(car1 + car2 + car3 + car4 + car5 + car6)

random_user_id()

