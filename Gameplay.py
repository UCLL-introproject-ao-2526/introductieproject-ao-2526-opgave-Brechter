from Cards import *
from Pointsystem import *
from Wallet import wallet, table

def BetAdd():
    wallet.AddMoney(-20)
    table.AddMoney(20)

def BetReset():
    totalbet = table.amount
    wallet.AddMoney(totalbet)
    table.AddMoney(-totalbet)


