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





# Class - __init__
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





# Class - __str__
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





# Class - Getter & Setter
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





# Class - @classmethod
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

