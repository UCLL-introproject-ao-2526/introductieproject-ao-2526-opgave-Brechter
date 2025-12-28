from Globals import *

#this class handles everything with money
class Bundle:
    def __init__(self, money):
        self.__amount = money

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, value):
        self.__amount = value

    def AddMoney(self, money):
        self.amount += money

    
    #time to define functions

#these are global objects from the bundle class
wallet = Bundle(1000)
table = Bundle(0)
insurance = Bundle(0)

#this function adds 20 coins from the wallet to the table
def BetAdd():
    if wallet.amount >= 20:
        wallet.AddMoney(-20)
        table.AddMoney(20)

#this function resets the table and gives the money back to the player
def BetReset():
    totalbet = table.amount
    wallet.AddMoney(totalbet)
    table.AddMoney(-totalbet)

#this function is called when insurance is bought
def Betinsurance():
    totalbet = table.amount//2
    if wallet.amount >= totalbet:
        wallet.AddMoney(-totalbet)
        insurance.AddMoney(totalbet)
        return True

#this function pays the player back according to the result of the round
def Payout(state, dealerbj=False, insur=False):
    #loss: 0, draw: 1, win: 2, blackjack: 3
    totalbet = table.amount
    wallet.AddMoney(state*totalbet)
    if state == 3:
        wallet.AddMoney(-(totalbet//2))
    table.AddMoney(-totalbet)
    if dealerbj and insur:
        insurancebet = insurance.amount
        insurance.AddMoney(-insurancebet)
        wallet.AddMoney(2*insurancebet)


    #time to define the animating function

#this function animates the coin going up. It's used for betting, insurance and coinfest
def Coinanimation(screen, objfrtuple, x=MIDW, y=MIDH):
    x = x+37
    object, frame = objfrtuple
    if frame <= 15:
        center = object.get_rect(center = (x, y-(frame*2)))
        screen.blit(object, center)
        frame += 1
    return (object, frame)