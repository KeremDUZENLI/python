
#_____CREATING LIST_____#

names = []

for _ in range(3):
    names.append(input("What's your name? "))


for i in sorted(names):
    print(f"hello, {i}")





#_____CREATE TXT 1_____#

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()





#_____CREATE TXT 2_____#

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")





#_____READING TXT_____#

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())





#_____READING TXT AND SORTING_____#

liste = []

with open("names.txt", "r") as file:
    for line in file:
        liste.append(line.rstrip())

for name in sorted(liste):
    print(f"hello, {name}")





#_____READING CSV_____#

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")





#_____SORTING CSV_____#

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for _ in sorted(students):
    print(_)





#_____SORTING CSV BY VALUE_____#

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")





#_____LAMBDA_____#

students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")





#_____CSV READER_____#

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")





#_____CSV DICTREADER_____#

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")





#_____CSV CREATE_____#

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    x = csv.DictWriter(file, fieldnames=["name", "home"])
    x.writerow({"name": name, "home": home})





#_____ANIMATION_____#

import sys

from PIL import Image

links = []

for arg in sys.argv[1:]:
    moment = Image.open(arg)
    links.append(moment)


links[0].save("costumes2.gif", save_all=True, append_images=[links[1]], duration=200, loop=0)




