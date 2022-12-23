# ---------- MANEJO DE FICHEROS ----------- #
import os

#.txt file
txt_file = open("file.txt", "w+")
txt_file.write("Mi nombre es Lautaro\nMi apellido es Bustos\nTengo 22 años\nMi lenguaje de programacion es Python")
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readlines())
#for line in txt_file.readlines():
#    print(line)

#txt_file.write("\n no se que poner")
#print(txt_file.readline())

txt_file.close()

#os.remove("file.txt")

# json.file
import json

json_file = open("objects.json", "w+")

json_test = {
    "Nombre": "Lautaro",
    "Apellido": "Bustos",
    "Edad": 23
}

json.dump(json_test, json_file, indent = 4)

json_file.close()

with open ("objects.json") as otro_json: 
    for line in otro_json.readlines():
        print(line)

json_dict = json.load(open("objects.json"))
print(type(json_dict))

#.csv file
import csv

csv_file = open("objects.csv", "w+")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["nombre", "apellido", "edad"])
csv_writer.writerow(["Lautaro", "Bustos", 23])

csv_file.close()

with open ("objects.csv") as otro_csv: 
    for line in otro_csv.readlines():
        print(line)

#.xml file
import xml

#.xlsx file
#import xlrd


# ---------- EJERCICIOS ----------- #






