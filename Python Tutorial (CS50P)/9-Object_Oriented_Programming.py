
# Tuple
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name    = input("Name: ")
    house   = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()





# List
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name  = input("Name: ")
    house = input("House: ")
    return [name, house]


if __name__ == "__main__":
    main()





# Dictionary 1
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"]  = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()





# Dictionary 2
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name  = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()


#----------------------------------------------------------------------------------------


# __init__
class Student:
    def __init__(self, name, house):
        self.name  = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name    = input("Name: ")
    house   = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()





# __str__
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name     = name
        self.house    = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        if self.patronus == "Stag":
            return "🐴"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus == "Jack Russell terrier":
            return "🐶"
        else:
            return "✨"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name     = input("Name: ")
    house    = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()





# Getter & Setter
class Student:
    def __init__(self, name, house):
        self.name  = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @property
    def house(self):
        return self._house

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name  = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()





# @classmethod
class Student:
    def __init__(self, name, house):
        self.name  = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name  = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()





import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")





import random

class Hat:
    
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")





# Inheritance
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizard    = Wizard("Albus")
student   = Student("Harry")
professor = Professor("Severus")





#   BaseException
#       KeyboardInterrupt
#       Exception
#           ArithmeticError
#               ZeroDivisionError
#           AssertionError
#           EOFError
#           ImportError
#               ModuleNotFoundError
#           LookupError
#               KeyError
#           NameError
#           SyntaxError
#               IndentationError
#           ValueError





# Operator Overloading
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles  = sickles
        self.knuts    = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)


galleons = potter.galleons + weasley.galleons
sickles  = potter.sickles + weasley.sickles
knuts    = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)





class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles  = sickles
        self.knuts    = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles  = self.sickles  + other.sickles
        knuts    = self.knuts    + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)
