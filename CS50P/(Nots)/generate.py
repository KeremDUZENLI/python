import random



coin = random.choice(["head", "tails"])
print(coin)


number = random.randint(1,10)
print(number)


cards = ["jack", "quenn", "king"]
random.shuffle(cards)
for _ in cards:
    print(_)


