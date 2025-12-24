import pygame as pg
from Wallet import *
from Cards import *
from Pointsystem import *
from Setup import *


#intialising
pg.init()
pg.display.set_caption("Blackjack")
from Globals import *


def dealerplay(dealerhand):
    global game_end
    if 0 <= dealerhand.score < 17:
        dealerhand.retrieve()
        game_end = False

def drawcards(phand, dhand):
    plen = len(phand.cards)
    dlen = len(dhand.cards)
    pxpos = HAND_POS_X_EVEN if plen %2 == 0 else HAND_POS_X_ODD
    dxpos = HAND_POS_X_EVEN if dlen %2 == 0 else HAND_POS_X_ODD
    for i in range(plen):
        simulatecard(pxpos[i], PHAND_POS_Y, phand.cards[i])
    for j in range(dlen):
        simulatecard(dxpos[j], DHAND_POS_Y, dhand.cards[j])

def drawgame(active, betting):
    
    #getting globals and making variables
    global winscreen
    global losescreen
    global tiedscreen  
    global insurask
    global insur
    button_list = []

    #startscreen
    if not active:
        play = pg.draw.circle(screen, color=BUTTON_COLOR, radius=75, center=(MIDW, MIDH))
        playtext = FONT.render('PLAY', True, BUTTON_TEXT_COLOR)
        screen.blit(playtext, (MIDW-56, MIDH-18))
        button_list.append(play)
    
    #once the game starts, you go to the betting menu
    else:

        #setting up the standard text during the game
        wallettext = FONT_SMALL.render(f'Wallet: {wallet.amount}', True, TEXT_COLOR)
        screen.blit(wallettext, (10, 10))
        betamounttext = FONT_SMALL.render(f'Bet: {table.amount}', True, TEXT_COLOR) 
        screen.blit(betamounttext, (10, 30))
        if insur:
            insurancetext = FONT_SMALL.render(f'Insurance: {insurance.amount}', True, TEXT_COLOR) 
            screen.blit(insurancetext, (10, 50))

        #the betting menu
        if betting:
            bet = pg.draw.circle(screen, color=BUTTON_COLOR, radius=75, center=(MIDW, (MIDH+HEIGHT)//2))
            bettext = FONT.render('BET', True, BUTTON_TEXT_COLOR)
            screen.blit(bettext, (MIDW-44, (MIDH+HEIGHT)//2-18))
            reset = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(MIDW-100, MIDH//4))
            resettext = FONT_SMALL.render('RESET', True, BUTTON_TEXT_COLOR)
            screen.blit(resettext, (MIDW-130, MIDH//4-9))
            start = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(MIDW+100, MIDH//4))
            starttext = FONT_SMALL.render('START', True, BUTTON_TEXT_COLOR)
            screen.blit(starttext, (MIDW+70, MIDH//4-9))
            button_list.append(bet)
            button_list.append(reset)
            button_list.append(start)

        #if the game ends
        elif winscreen:
            screen.fill(WIN_COLOR)
            endtext = FONT_BIG.render('YOU WON', True, TEXT_COLOR)
            screen.blit(endtext, (MIDW-250, MIDH-50))
        elif losescreen:
            screen.fill(LOSE_COLOR)
            endtext = FONT_BIG.render('YOU LOST', True, TEXT_COLOR)    
            screen.blit(endtext, (MIDW-260, MIDH-50))
        elif tiedscreen:
            screen.fill(TIED_COLOR)
            endtext = FONT_BIG.render("IT'S A TIE", True, TEXT_COLOR)  
            screen.blit(endtext, (MIDW-240, MIDH-50))

        #during the game itself
        else:
            if phand.score != 100:
                scoretext = FONT_SMALL.render(f'Score: {phand.score if phand.score != -1 else "Dead"}', True, TEXT_COLOR)
            else:
                scoretext = FONT_SMALL.render(f'Score: Winner! (7 cards)', True, TEXT_COLOR)
            screen.blit(scoretext, (10, HEIGHT-30))
            deckimg = pg.image.load("Card_designs\Back_card.png")
            screen.blit(deckimg, (DECK_POS_X, DECK_POS_Y))
            hit = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(WIDTH//6, (MIDH+3*HEIGHT)//4))
            hittext = FONT_SMALL.render('HIT', True, BUTTON_TEXT_COLOR)
            screen.blit(hittext, (WIDTH//6-15, (MIDH+3*HEIGHT)//4-9))
            stand = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(5*WIDTH//6, (MIDH+3*HEIGHT)//4))
            standtext = FONT_SMALL.render('STAND', True, BUTTON_TEXT_COLOR)
            screen.blit(standtext, (5*WIDTH//6-30, (MIDH+3*HEIGHT)//4-9))
            drawcards(phand, dhand)
            button_list.append(hit)
            button_list.append(stand)

            #if the first card is an ace the player will be asked to buy insurance, if the dealer gets a blackjack, the player will get double the insurance back
            if insurask:
                ins_y = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(50, MIDH))
                ins_n = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(150, MIDH))
                yestext = FONT_SMALL.render('YES', True, BUTTON_TEXT_COLOR)
                notext = FONT_SMALL.render('NO', True, BUTTON_TEXT_COLOR)
                screen.blit(yestext, (32, MIDH-9))
                screen.blit(notext, (137, MIDH-9))
                instext = FONT_SMALL.render('INSURANCE?', True, TEXT_COLOR)
                screen.blit(instext, (40, MIDH-80))
                button_list.append(ins_y)
                button_list.append(ins_n)
    return button_list


def play():
    #setting up
    run = True
    frame = 0

    #main game loop
    while run:
        frame += 1
        timer.tick(FPS)
        screen.fill(BG_COLOR)

        #globals and variables
        global playing
        global betting
        global dealerturn
        global dealerturn_init
        global game_end
        global losescreen
        global winscreen
        global tiedscreen
        global insurask
        global insur
        global playerdead
        global phand
        button_list = drawgame(playing, betting)
        
        #to check if the player dies
        if not playerdead and phand.score == -1:
            playerdead = True
            frame = 0
        
        #once the player dies they get one second before the dealer reveals his card
        if playerdead and frame > 60:
            dealerturn_init = True
            dhand.cards[1].reveal()

        #3 seconds after the game ends, the endscreen will appear
        if game_end and frame > 180:
            dealerturn = False
            gamestate, dblackjack = CompareScores(phand.score, dhand.score)
            if gamestate == 0:
                losescreen = True
            elif gamestate == 1:
                tiedscreen = True
            else:
                winscreen = True
            Payout(gamestate, dblackjack)
            frame = 0
            game_end = False

        #5 seconds after the endscreen a new game will begin
        if (winscreen or tiedscreen or losescreen) and frame > 300:
            frame = 0
            winscreen, tiedscreen, losescreen = False, False, False
            dhand.empty()
            phand.empty()
            betting = True
            playerdead = False

        #the dealer's turn begins with him flipping his card and every second he'll draw a new one until he decides to end the game
        if dealerturn_init and frame > 60:
            frame = 0
            dealerturn_init = False
            dealerturn = True
        if dealerturn and frame > 60 and not game_end and not (winscreen or tiedscreen or losescreen):
            frame = 0
            game_end = True
            dealerplay(dhand)

        #checking clicks
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONUP:
                    
                #startscreen
                if not playing:
                    if button_list[0].collidepoint(event.pos):
                        betting = True
                        playing = True
                        button_list = drawgame(playing, betting)
                    
                #betting stage
                elif playing and betting:
                    if button_list[0].collidepoint(event.pos):
                        BetAdd()
                    if button_list[1].collidepoint(event.pos):
                        BetReset()
                    if button_list[2].collidepoint(event.pos):
                        game_end = False
                        betting = False

                        #at the end of the betting stage, the cards will be prepared
                        insurask = setup()

                #now it's the player's turn
                if not playerdead:
                    if playing and not betting:
                        if button_list[0].collidepoint(event.pos) and not (dealerturn_init or dealerturn):
                            phand.retrieve()
                            if insurask:
                                insurask = False
                        if button_list[1].collidepoint(event.pos) and not (dealerturn_init or dealerturn):
                            dealerturn_init = True
                            frame = 0
                            dhand.cards[1].reveal()
                            if insurask:
                                insurask = False
                        if insurask:
                            if button_list[2].collidepoint(event.pos):
                                insurask = False
                                insur = Betinsurance()
                            if button_list[3].collidepoint(event.pos):
                                insurask = False

                
    #end of loop   
        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    play()