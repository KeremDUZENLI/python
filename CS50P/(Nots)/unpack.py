# Unpack
first, last = input("What's your name?").split(" ")
print(f"hello, {first}")


# Unpack List
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")
print(total(*coins), "Knuts")


# Unpack Dict
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
print(total(**coins), "Knuts")


# Args
def f(*args, **kwargs):
    print("Positional: ", args)


f(100, 50, 25, 5)


# Kwargs
def f(*args, **kwargs):
    print("Named: ", kwargs)


f(galleons=100, sickles=50, knuts=25)
