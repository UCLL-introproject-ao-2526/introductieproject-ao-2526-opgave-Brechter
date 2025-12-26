from Cards import *
from Globals import *

deck = Deck()
phand = Hand(deck)
dhand = Hand(deck, False)

def setup(n):
    if n <= 2:
        phand.retrieve()
        return False
    elif n == 3:
        dhand.retrieve()
        return False
    elif n == 4:
        dhand.retrieve(True)
        if dhand.cards[1].number == "A":
            return True
        else:
            return False