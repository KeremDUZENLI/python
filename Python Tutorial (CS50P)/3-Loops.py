
#_____LOOP PRINT_____#

print("meow\n" * 3, end="")





#_____LOOP WHILE_____#

i = 0
while i < 3:
    print("meow")
    i += 1





#_____LOOP FOR_____#

for _ in range(3):
    print("meow")





#_____LOOP CONDITION_____#
 
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")





#_____LOOP FUNCTION_____#

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()





#_____LOOP FUNCTION PRINT 1_____#

def main():
    print_column(3)
    print_row(4)
    print_square(3)


def print_column(height):
    print("#\n" * height, end="")


def print_row(width):
    print("?" * width, end="")


def print_square(size):

    # For each row in square
    for i in range(size):
        print()

        # For each brick in row
        for j in range(size):
            print("#", end="")


main()





#_____LOOP FUNCTION PRINT 2_____#

def main():
    number = get_number()
    print_square(number)
    

def print_square(size):
    for i in range(size):
        print("#" * size)


def get_number():
    n = int(input("What's n? "))
    return n


main()





#_____DICTIONARY_____#

students = {"Hermonie": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}

for i in students:
    print(i, students[i], sep=", ")





#_____LIST_____#

students = [
    {"name": "Hermon", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for i in students:
    print(i["name"], i["house"], i["patronus"], sep="\t\t")
