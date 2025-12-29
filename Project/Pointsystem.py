from Globals import *

#this function checks a card and updates Points and Aces in the hand
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
    
#this function uses the points and the aces of the hand to calculate the score
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
    
#this function decides if the game is won, lost, tied and if there are any blackjacks
def CompareScores(Player, Dealer):
    if Player == 21 and Dealer != 21:
        return 3
    elif Dealer == 21 and Player != 21:
        return 0
    else:
        if Player != -1:
            return int(Player >= Dealer) + int(Player > Dealer)
        else:
            return 0