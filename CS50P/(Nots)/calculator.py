""" 
x = float(input("What's x? "))
y = float(input("What's y? "))


z = round(x + y)
print(f"{z:,}")

t = round(x / y, 2)
print(f"{t}")

r = x / y
print(f"{r:.2f}")
"""


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()
