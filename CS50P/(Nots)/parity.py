def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


""" 
# Method-1
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
"""
""" 
# Method-2
def is_even(n):
    return True if n % 2 == 0 else False
"""

# Method-3
def is_even(n):
    return (n % 2 == 0)



main()
