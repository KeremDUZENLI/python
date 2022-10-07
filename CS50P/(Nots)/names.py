"""
# For loop for creating list
names = []

for _ in range(3):
    names.append(input("What's your name? "))


for i in sorted(names):
    print(f"hello, {i}")
"""

"""
# Open and save txt - 1
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""

""" 
# Open and save txt - 2
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""

""" 
# Reading txt
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
"""


# Reading txt and sorting
liste = []

with open("names.txt", "r") as file:
    for line in file:
        liste.append(line.rstrip())

for name in sorted(liste):
    print(f"hello, {name}")

