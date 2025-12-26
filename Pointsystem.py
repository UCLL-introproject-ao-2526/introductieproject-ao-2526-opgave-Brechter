from Globals import *

def AddPoints(card, Points=0, Aces=0):
    if not 0 <= Points <= 21:
        return -1, Aces
    else:
        if card.number in ["2", "3", "4", "5", "6", "7", "8", "9"]:
            Points += int(card.number)
        elif card.number == 'A':
            Aces += 1
        else:
            Points += 10
    return Points, Aces
    
def TotalPoints(Score, Aces):
    Score += Aces
    while Aces > 0:
        if Score <= 11:
            Score += 10
        Aces -= 1
    if Score > 21 and Score != 100:
        return -1
    else:        
        return Score
    
def CompareScores(Player, Dealer): #dealerblackjack = -2, loss = -1, tie = 0, win = 1, blackjack = 2
    if Player == 21:
        return 3
    else:
        return int(Player >= Dealer) + int(Player > Dealer)