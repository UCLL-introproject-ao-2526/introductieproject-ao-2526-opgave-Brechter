from Cards import *
from Globals import *

deck = Deck()
phand = Hand(deck)
dhand = Hand(deck, False)

def setup():
    for i in range(2):
        phand.retrieve()
    dhand.retrieve()
    dhand.retrieve(True)
    if dhand.cards[0].number == "A":
        return True