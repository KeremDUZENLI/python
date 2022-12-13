"""
# Function-1
def main():
    print_column(3)
    print_row(4)
    print_square(3)


def print_column(height):
    print("#\n" * height, end="")


def print_row(width):
    print("?" * width)


def print_square(size):

    # For each row in square
    for i in range(size):
        print()

        # For each brick in row
        for j in range(size):
            print("#", end="")


main()
"""


# Function-2
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

