""" 
name = input("What's your name? ").strip()

if "," in name:
    last, name = name.split(", ")
    name = f"{name} {last}"

print(f"hello, {name}")
"""

""" 
import re
name = input("What's your name? ").strip()
matches = re.search("^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
"""


import re
name = input("What's your name? ").strip()
if matches := re.search("^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")


