from Cards import *
from Pointsystem import *
from Globals import simulatecard, MIDH, MIDW

class Hand:
    def __init__(self, deck, playerhand = True):
        self.deck = deck
        self.__points = 0
        self.__aces = 0
        self.cards = []
        self.playerhand = playerhand
        
    
    @property
    def points(self):
        return self.__points
    
    @property
    def aces(self):
        return self.__aces
    
    @points.setter
    def points(self, value):
        self.__points = value

    @aces.setter
    def aces(self, value):
        self.__aces = value

    @property
    def score(self):
        scor = TotalPoints(self.points, self.aces)
        return scor
    
    def retrieve(self):
        card = self.deck.draw()
        simulatecard(MIDW, MIDH, card)
        self.points, self.aces = AddPoints(card, self.points, self.aces)
        

    


    



