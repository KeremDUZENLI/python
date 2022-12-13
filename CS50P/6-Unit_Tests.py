
#_____UNIT TEST 1_____#

from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


if __name__ == "__main__":
    main()


# calculator =

#   def main():
#       x = int(input("What's x? "))
#       print("x squared is", square(x))

#   def square(n):
#       return n * n


#   if __name__ == "__main__":
#       main()





#_____UNIT TEST 2_____#

from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0


# calculator =

#   def main():
#       x = int(input("What's x? "))
#       print("x squared is", square(x))

#   def square(n):
#       return n * n


#   if __name__ == "__main__":
#       main()





#_____UNIT TEST LOOP_____#

from hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_arguments():
    for i in ["Hermione", "Harry", "Ron"]:
        assert hello(i) == f"Hello, {i}"


# hello =

#   def main():
#       name = input("What's your name? ")
#       print(hello(name))

#   def hello(to="world"):
#       return f"Hello, {to}"


#   if __name__ == "__main__":
#       main()




