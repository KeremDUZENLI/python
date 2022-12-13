""" 
url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
"""

""" 
import re
url = input("URL: ").strip()

username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
"""

""" 
import re

url = input("URL: ").strip()

matches = re.search("^(https?://)?(www\.)?twitter\.com/(.+)", url, re.IGNORECASE)

if matches:
    print(f"Username:", matches.group(3))
"""

""" 
import re

url = input("URL: ").strip()

if matches := re.search("^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
"""

