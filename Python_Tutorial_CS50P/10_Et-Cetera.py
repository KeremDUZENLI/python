### VARIABLES ##################################
################################################

MEOWS = 3


for _ in range(MEOWS):
    print("meow")


# Constant Variables
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()


### DOCSTRING ##################################
################################################


def meow(n: int) -> str:
    """
    Meow n times.

    :param n        : Number of times to meow
    :type n         : int
    :raise TypeError: If n is not an int
    :return         : A string of n meows, one per line
    :rtpe           : str
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")


### SYS ########################################
################################################

import sys


if len(sys.argv) == 1:
    print("meow")

elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])

    for _ in range(n):
        print("meow")

else:
    print("usage: meows.py")


### ARGPARSE ###################################
################################################

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow")
args = parser.parse_args()


for _ in range(int(args.n)):
    print("meow")


### UNPACK #####################################
################################################

first, last = input("What's your name?").split(" ")
print(f"hello, {first}")


# Unpack List
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")
print(total(*coins), "Knuts")


# Unpack Dict
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
print(total(**coins), "Knuts")


### ARGS - KWARGS ##############################
################################################

# Args
def f(*args, **kwargs):
    print("Positional: ", args)


f(100, 50, 25, 5)


# Kwargs
def f(*args, **kwargs):
    print("Named: ", kwargs)


f(galleons=100, sickles=50, knuts=25)


### COMPREHENSIONS #############################
################################################


# List Comprehensions
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()


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


### MAP ########################################
################################################

# Yell 1
def main():
    yell("This is CS50")


def yell(phase):
    print(phase.upper())


if __name__ == "__main__":
    main()


# Yell 2
def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(uppercased)
    print(*uppercased)


if __name__ == "__main__":
    main()


# Yell 3
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(uppercased)
    print(*uppercased)


if __name__ == "__main__":
    main()


# Map
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()


### FILTER #####################################
################################################

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


### LAMBDA #####################################
################################################

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


### ENUMERATE ##################################
################################################


# Enumerate 1
students = ["Hermonie", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])


# Enumerate 2
students = ["Hermonie", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)


### GENERATORS #################################
################################################


# Generators 1
n = int(input("What's n? "))

for i in range(n):
    print("🐑" * i)


# Generators 2
def main():
    n = int(input("What's n? "))

    for i in range(n):
        print("🐑" * i)


if __name__ == "__main__":
    main()


# Generators 3
def main():
    n = int(input("What's n? "))

    for i in range(n):
        print(sheep(i))


def sheep(n):
    return "🐑" * n


if __name__ == "__main__":
    main()


# Generators 4
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()


# Generators 5
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()


### VOICE TALK #################################
################################################

import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")

cowsay.cow(this)
engine.say(this)
engine.runAndWait()
