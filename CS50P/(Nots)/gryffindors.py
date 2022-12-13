#
students = [
    {"name": "Hermonie", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]
print(gryffindors)

for gryffindor in sorted(gryffindors):
    print(gryffindor)


# Filter
students = [
    {"name": "Hermonie", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in gryffindors:
    print(gryffindor["name"])


# Lambda
students = [
    {"name": "Hermonie", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in gryffindors:
    print(gryffindor["name"])


# Dictionary Comprehensions 1
students = ["Hermonie", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)


# Dictionary Comprehensions 2
students = ["Hermonie", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)


# Dictionary Comprehensions 3
students = ["Hermonie", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)


# Enumerate 1
students = ["Hermonie", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])


# Enumerate 2
students = ["Hermonie", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)
