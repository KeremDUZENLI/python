""" 
# Check 1
email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")
"""

""" 
# Check 2
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")
"""


# Regular Expression
import re

email = input("What's your email? ").strip()

if re.search("^\w+@(\w+\.)?\w\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


