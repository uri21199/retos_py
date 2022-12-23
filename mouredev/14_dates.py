# ---------- DATES ----------- #
from datetime import datetime

def print_date(date):
    print(date)
    print(date.year)
    print(date.day)
    print(date.month)
    print(date.hour)
    print(date.minute)
    print(date.timestamp())

now = datetime.now()

print_date(now)

timestamp = now.timestamp()

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

from datetime import time

current_time = time(21, 6, 10)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2022, 11, 10)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

from datetime import timedelta

time_delta = timedelta(200, 10, 100, weeks = 10)
time_delta2 = timedelta(300, 10, 100, weeks = 13)

print(time_delta2 - time_delta)
print(time_delta2 + time_delta)


# ---------- EJERCICIOS ----------- #
#1 - 2 -3
ahora = datetime.now()
print(ahora)
print(ahora.strftime("%d/%m/%Y %H:%M:%S"))

#4
diferencia = year_2023 - ahora
print(diferencia)

#5
year_1973 = datetime(1970, 1, 1)
diferencia = year_1973 - ahora
print(diferencia)





