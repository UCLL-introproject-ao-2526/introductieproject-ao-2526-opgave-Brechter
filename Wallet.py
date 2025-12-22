#dit is de klasse die alles met geld afhandelt
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

#dit zijn de relevante bundles
wallet = Bundle(100)
table = Bundle(0)
insurance = Bundle(0)

#hier de functies om dingen te doen met de wallet
def BetAdd():
    if wallet.amount >= 20:
        wallet.AddMoney(-20)
        table.AddMoney(20)

def BetReset():
    totalbet = table.amount
    wallet.AddMoney(totalbet)
    table.AddMoney(-totalbet)

def Betinsurance():
    totalbet = table.amount//2
    if wallet.amount >= totalbet:
        wallet.AddMoney(-totalbet)
        insurance.AddMoney(totalbet)

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