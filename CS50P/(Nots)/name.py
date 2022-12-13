import sys

""" 
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
"""


if len(sys.argv) < 2:
    sys.exit("Too few argumants")

for i in sys.argv[1:]:
    print("hello, my name is", i)

