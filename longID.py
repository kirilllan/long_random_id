# number of output digits slightly varies
import random

def longRandomID(iterations):
    yourId = ""
    while (iterations > 0):
        iterations -= 1
        yourId += str(random.getrandbits(16))
    print(yourId)  # remove if not needed
    return yourId

longRandomID(3)