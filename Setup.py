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
        
def ruleswritten(screen):
    with open('Rules.txt', 'r') as file:
        lines = file.readlines()
        ycoord = 10
        for line in lines:
            line.strip()
            if line[0] == "=":
                text = FONT_SMALL.render(line[1:-1], True, TEXT_COLOR)
                ycoord += 30
            else:
                text = FONT_TINY.render(line[:-1], True, TEXT_COLOR)
                ycoord += 20
            center = text.get_rect(center = (MIDW, ycoord))
            screen.blit(text, center)