
#_____CHANGE PLACE_____#

name = input("What's your name? ").strip()

if "," in name:
    last, name = name.split(", ")
    name = f"{name} {last}"

print(f"hello, {name}")





#_____CHECK 1_____#

email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")





#_____CHECK 2_____#

email = input("What's your email? ").strip()

username, domain = email.split("@")

if "." in domain:
    print("Valid")
else:
    print("Invalid")





#_____CHECK NAMES 1_____#

import re
name = input("What's your name? ").strip()
matches = re.search("^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")





#_____CHECK NAMES 2_____#

import re
name = input("What's your name? ").strip()
if matches := re.search("^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")





#_____REPLACE_____#

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")





#_____REGEX SUB_____#

import re
url = input("URL: ").strip()

username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")





#_____REGULAR EXPRESSION_____#

import re

email = input("What's your email? ").strip()

if re.search("^(.+)@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")





#_____REGEX SEARCH 1_____#

import re

url = input("URL: ").strip()

matches = re.search("^(https?://)?(www\.)?twitter\.com/(.+)", url, re.IGNORECASE)

if matches:
    print(f"Username:", matches.group(3))





#_____REGEX SEARCH 2_____#

import re

url = input("URL: ").strip()

if matches := re.search("^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))




