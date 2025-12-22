import random as rd

SUITS = ["h", "d", "c", "s"]
NUMBERS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

class Card:
    def __init__(self, suit, number, revealed = True):
        self.__suit = suit
        self.__number = number
        self.revealed = revealed

    @property
    def suit(self):
        return self.__suit
    
    @property
    def number(self):
        return self.__number
    
    @property
    def revealed(self):
        return self.revealed
    
    @revealed.setter
    def revealed(self, value):
        self.revealed = value

    def reveal(self):
        self.revealed = True
    
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
            card = self.__cards.pop(-1).name
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

