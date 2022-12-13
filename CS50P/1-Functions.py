
#_____STRING TYPE_____#

name = input("What's your name? ").strip().title()

print(f"Hello, {name}")



#_____STRING FUNCTION_____#

def main():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()





#_____INTEGER TYPE_____#

x = float(input("What's x? "))
y = float(input("What's y? "))


z = round(x + y)
print(f"{z:,}")

t = round(x / y, 3)
print(f"{t}")

r = x / y
print(f"{r:.2f}")





#_____INTEGER FUNCTION_____#

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()




