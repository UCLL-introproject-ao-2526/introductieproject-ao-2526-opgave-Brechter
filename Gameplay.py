from Cards import *
from Pointsystem import *

class Hand:
    def __init__(self, deck, playerhand = True):
        self.deck = deck
        self.points = 0
        self.aces = 0
        self.cards = []
        self.playerhand = playerhand
        
    
    @property
    def points(self):
        return self.points
    
    @property
    def aces(self):
        return self.aces
    
    @points.setter
    def points(self, value):
        self.points = value

    @aces.setter
    def aces(self, value):
        self.aces = value

    @property
    def score(self):
        scor = TotalPoints(self.points, self.aces)
        return scor
    
    def retrieve(self):
        card = self.deck.draw()
        self.points, self.aces = AddPoints(card, self.points, self.aces)
        

    


    



