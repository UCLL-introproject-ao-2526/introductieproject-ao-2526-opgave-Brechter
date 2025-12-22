def AddPoints(card, Points=0, Aces=0):
    if Points > 21:
        return -1
    else:
        if card.number in ["2", "3", "4", "5", "6", "7", "8", "9"]:
            Points += int(card.number)
        elif card.number == 'A':
            Aces += 1
        else:
            Points += 10
    return Points, Aces
    
def TotalPoints(Score, Aces):
    while Aces > 0:
        if 21 - Score >= 11:
            Score += 11
        else:
            Score += 1
        Aces -= 1
    if Score > 21:
        return -1
    else:        
        return Score
    
def CompareScores(Player, Dealer): #dealerblackjack = -2, loss = -1, tie = 0, win = 1, blackjack = 2
    if Player == 21:
        return 3
    else:
        return int(Player >= Dealer) + int(Player > Dealer)
    
def Dealerbj(Dealer):
    return Dealer == 21
