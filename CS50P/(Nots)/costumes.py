import sys

from PIL import Image

links = []

for arg in sys.argv[1:]:
    moment = Image.open(arg)
    links.append(moment)


links[0].save(
    "costumes.gif", save_all=True, append_images=[links[1]], duration=200, loop=0
)
