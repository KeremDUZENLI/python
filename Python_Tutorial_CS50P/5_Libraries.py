
#_____RANDOM CHOICE_____#

import random

coin = random.choice(["head", "tails"])
print(coin)





#_____RANDOM RANDINT_____#

import random

number = random.randint(1,10)
print(number)





#_____RANDOM SHUFFLE_____#

import random

cards = ["jack", "quenn", "king"]
random.shuffle(cards)

for _ in cards:
    print(_)





#_____STATISTICS_____#

import statistics

print(statistics.mean([100, 90]))





#_____SYS_____#

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])





#_____SYS LOOP_____#

import sys

if len(sys.argv) < 2:
    sys.exit("Too few argumants")

for i in sys.argv[1:]:
    print("hello, my name is", i)





#_____SYS SAYINGS_____#

import sys
import sayings

if len(sys.argv) == 2:
    sayings.goodbye(sys.argv[1])


# sayings library =

#   def hello(name):
#       print(f"hello, {name}")

#   def goodbye(name):
#       print(f"goodbye, {name}")





#_____COWSAY_____#

import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])





#_____REQUESTS_____#

import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

x = response.json()

for i in x["results"]:
    print(i["trackName"])




