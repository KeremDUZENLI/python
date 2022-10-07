# 1
def main():
    yell("This is CS50")


def yell(phase):
    print(phase.upper())


if __name__ == "__main__":
    main()


# 2
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


# 3
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


# List Comprehensions
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
