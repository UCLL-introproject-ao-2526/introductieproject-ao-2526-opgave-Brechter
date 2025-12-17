import random as rd

SUITS = ["h", "d", "c", "s"]
NUMBERS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

class Card:
    def __init__(self, suit, number):
        self.__suit = suit
        self.__number = number

    @property
    def suit(self):
        return self.__suit
    
    @property
    def number(self):
        return self.__number
    
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
    def __init__(self, decks=1, shuffled=True):
        if decks < 0 or type(decks) != int:
            raise(ValueError)
        self.__cards = makenewdeck(decks)
        if shuffled:
            rd.shuffle(self.__cards)

    def draw(self):
        return self.__cards.pop(-1).name
    
    def __str__(self):
        str = ""
        for card in self.__cards:
            str += card.name + ' '
        return str[:-1]

