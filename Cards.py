import random as rd
import pygame as pg
from Pointsystem import *
from Globals import *


    #time to define classes

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

class Deck:
    def __init__(self, decks=4):
        if decks < 0 or type(decks) != int:
            raise(ValueError)
        self.__cards = makenewdeck(decks)
        rd.shuffle(self.__cards)
        self.__decks = decks
        self.__count = 0

    @property
    def count(self):
        return self.__count

    #this function is called whenever a new card is drawn or revealed, unrevealed cards won't be registered
    def cardcountupdate(self, card):
        if card.revealed:
            if card.number in ["A", "T", 'J', 'Q', 'K']:
                self.__count -= 1
            elif card.number in ["2", "3", "4", "5", "6"]:
                self.__count += 1

    #this function removes a card from the deck and returns that card
    #if the deck is empty it will make a new one and still return the card
    def draw(self, revealed = True):
        if not len(self.__cards) == 0:
            card = self.__cards.pop(-1)
            card.revealed = revealed
            self.cardcountupdate(card)
            return card
        else:
            self.__cards = makenewdeck(self.__decks)
            self.__count = 0
            rd.shuffle(self.__cards)
            return self.draw(revealed)
    


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
        if len(self.cards) < 7 or scor == -1:
            return scor
        elif len(self.cards) == 7 and scor == 21:
            return 21
        else:
            return 100
    
    #this function will draw a card from the deck
    def retrieve(self, hidden=False):
        card = self.deck.draw(not hidden)
        self.cards = add_to_list(card, self.cards)
        self.points, self.aces = AddPoints(card, self.points, self.aces)
        simulatecard(DECK_POS_X + 33, DECK_POS_Y + 48, card)
    
    #this function empties the hand which is needed at the end of a round
    def empty(self):
        self.__init__(self.deck, self.playerhand)


    #time to define globals

#these globals are only needed by functions in this file
SUITS = ["h", "d", "c", "s"]
NUMBERS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]


    #time to define functions

#this function makes a new deck n times using the globals in this file
def makenewdeck(n):
    deck = []
    for i in range(n):
        for suit in SUITS:
            for number in NUMBERS:
                deck.append(Card(suit, number))
    return deck

#this function is the brain of the dealer. As you can see, there's not a lot going on in there
#the return statements are for globals in Game.py
def dealerplay(dealerhand):
    if 0 <= dealerhand.score < 17:
        dealerhand.retrieve()
        return True, False, True
    else:
        return False, True, False

#this function deals the initial two cards 
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
        

    #time to define the card animating functions

#this function projects a single card
def simulatecard(xpos, ypos, card):
    xpos = xpos - 33
    ypos = ypos - 48
    if card.revealed:
        card_img = pg.image.load(f"Card_designs/{card.name}.png")
    else:
        card_img = pg.image.load("Card_designs/Back_card.png")
    screen.blit(card_img, (xpos, ypos))

#this function draws all cards in one hand
def drawcards(phand, dhand, plinvis=False, dlinvis=False):
        
        #it starts with the player
        if len(phand.cards) > 0:
            plen = len(phand.cards)
            pxpos = HAND_POS_X_EVEN if plen%2 == 0 else HAND_POS_X_ODD
            if plen%2==1:
                for i in range(plen - 1):
                    simulatecard(pxpos[i], PHAND_POS_Y, phand.cards[i])
                if not plinvis:
                    simulatecard(pxpos[plen - 1], PHAND_POS_Y, phand.cards[plen - 1])
            else:
                for i in range(plen):
                    if i != plen-2:
                        simulatecard(pxpos[i], PHAND_POS_Y, phand.cards[i])
                if not plinvis:
                    simulatecard(pxpos[plen - 2], PHAND_POS_Y, phand.cards[plen - 2])
        
        #now for the dealer
        if len(dhand.cards) > 0:    
            dlen = len(dhand.cards)
            dxpos = HAND_POS_X_EVEN if dlen %2 == 0 else HAND_POS_X_ODD
            if dlen%2 == 1:
                for j in range(dlen - 1):
                    simulatecard(dxpos[j], DHAND_POS_Y, dhand.cards[j])
                if not dlinvis:
                    simulatecard(dxpos[dlen - 1], DHAND_POS_Y, dhand.cards[dlen - 1])
            else:
                for i in range(dlen):
                    if i != dlen-2:
                        simulatecard(dxpos[i], DHAND_POS_Y, dhand.cards[i])
                if not dlinvis:
                    simulatecard(dxpos[dlen - 2], DHAND_POS_Y, dhand.cards[dlen - 2])

#this function animates a card going from the deck to the right place in the hand
def cardanimation(phand, dhand, frame, pcardanim):
    eposx = 0
    eposy = 0
    card = None
    if pcardanim:
        handsize = len(phand.cards)-1
        eposy = PHAND_POS_Y
        eposx = HAND_POS_X_EVEN[handsize-1] if (handsize+1)%2 == 0 else HAND_POS_X_ODD[handsize]
        card = phand.cards[2*(handsize//2)]
    else:
        handsize = len(dhand.cards)-1
        if handsize > -1:
            eposy = DHAND_POS_Y
            eposx = HAND_POS_X_EVEN[handsize-1] if (handsize+1)%2 == 0 else HAND_POS_X_ODD[handsize]
            card = dhand.cards[2*(handsize//2)]
    bposx = MIDW
    bposy = MIDH
    xpos = ((15-frame)*bposx + frame*eposx)//15
    ypos = ((15-frame)*bposy + frame*eposy)//15
    if not card == None:
        simulatecard(xpos, ypos, card)


    #time to define global objects

deck = Deck()
phand = Hand(deck)
dhand = Hand(deck, False)