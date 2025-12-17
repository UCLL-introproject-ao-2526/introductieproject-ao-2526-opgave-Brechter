from Cards import *
from Pointsystem import *
from Wallet import wallet, table

class Hand:
    def __init__(self):
        self.hand = []
        self.Points = 0
        self.Aces = 0
        self.Score = 0

    def AddCard(self, card):
        self.hand.append(card)
        self.EvaluateScore(card)

    def EvaluateScore(self, card):
        self.Points, self.Aces = AddPoints(card, self.Points, self.Aces)
        self.Score = TotalPoints(self.Points, self.Aces)

def BetAdd():
    wallet.AddMoney(-20)
    table.AddMoney(20)

def Play():
    deck = Deck(4)
    card = Deck.draw()
