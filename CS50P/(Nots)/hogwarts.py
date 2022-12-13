""" 
# List
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i+1, students[i])
"""

""" 
# Dictionary
students = {
    "Hermonie": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
    }

for i in students:
    print(i, students[i], sep=", ")
"""

students = [
    {"name": "Hermonie", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for i in students:
    print(i["name"], i["house"], i["patronus"], sep="\t")
