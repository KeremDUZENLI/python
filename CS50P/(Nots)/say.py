import cowsay
import sys

""" 
if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
"""


import sayings

if len(sys.argv) == 2:
    sayings.goodbye(sys.argv[1])

