import random as rd
from Pointsystem import *
from Globals import *

SUITS = ["h", "d", "c", "s"]
NUMBERS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

class Card:
    def __init__(self, suit, number, revealed = True):
        self.__suit = suit
        self.__number = number
        self.__revealed = revealed

    @property
    def suit(self):
        return self.__suit
    
    @property
    def number(self):
        return self.__number
    
    @property
    def revealed(self):
        return self.__revealed
    
    @revealed.setter
    def revealed(self, value):
        self.__revealed = value

    def reveal(self):
        self.__revealed = True
    
    @property
    def name(self):
        return self.__suit + self.__number
    
def makenewdeck(n):
    deck = []
    for i in range(n):
        for suit in SUITS:
            for number in NUMBERS:
                deck.append(Card(suit, number))
    return deck

class Deck:
    def __init__(self, decks=4):
        if decks < 0 or type(decks) != int:
            raise(ValueError)
        self.__cards = makenewdeck(decks)
        rd.shuffle(self.__cards)
        self.__decks = decks

    def draw(self, revealed = True):
        if not len(self.__cards) == 0:
            card = self.__cards.pop(-1)
            card.revealed = revealed
            return card
        else:
            self.__cards = makenewdeck(self.__decks)
            rd.shuffle(self.__cards)
            return self.draw(revealed)
    
    def __str__(self):
        str = ""
        for card in self.__cards:
            str += card.name + ' '
        return str[:-1]

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
        if len(self.cards) < 7:
            scor = TotalPoints(self.points, self.aces)
            return scor
        else:
            return 100
    
    def retrieve(self, hidden=False):
        card = self.deck.draw(not hidden)
        self.cards.append(card)
        simulatecard(DECK_POS_X + 33, DECK_POS_Y + 48, card)
        self.points, self.aces = AddPoints(card, self.points, self.aces)
    
    def empty(self):
        self.__init__(self.deck, self.playerhand)