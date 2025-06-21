
#_____COMPARE_____#

x = int(input("What's x? "))
y = int(input("What's y? "))


if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")





#_____CONDITION_____#

x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}")





#_____CONDITION CHAIN_____#

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")

elif score >= 80:
    print("Grade: B")

elif score >= 70:
    print("Grade: C")

elif score >= 60:
    print("Grade: D")

else:
    print("Grade: F")






#_____CONDITION FUNCTION 1_____#

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()





#_____CONDITION FUNCTION 2_____#

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()





#_____CONDITION FUNCTION 3_____#

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return (n % 2 == 0)

main()




