import pygame as pg
from Gameplay import Hand
from Wallet import *
from Cards import *



#intialising
pg.init()
pg.display.set_caption("Blackjack")
from Globals import *

deck = Deck()
phand = Hand(deck)

def drawgame(active, betting, insur=False, hand=None):
    button_list = []
    if not active:
        play = pg.draw.circle(screen, color=BUTTON_COLOR, radius=75, center=(MIDW, MIDH))
        playtext = FONT.render('PLAY', True, BUTTON_TEXT_COLOR)
        screen.blit(playtext, (MIDW-56, MIDH-18))
        button_list.append(play)
    else:
        wallettext = FONT_SMALL.render(f'Wallet: {wallet.amount}', True, TEXT_COLOR)
        screen.blit(wallettext, (10, 10))
        betamounttext = FONT_SMALL.render(f'Bet: {table.amount}', True, TEXT_COLOR) 
        screen.blit(betamounttext, (10, 30))
        if insur:
            insurancetext = FONT_SMALL.render(f'Bet: {table.amount}', True, TEXT_COLOR) 
            screen.blit(betamounttext, (10, 50))
        if betting:
            bet = pg.draw.circle(screen, color=BUTTON_COLOR, radius=75, center=(MIDW, (MIDH+HEIGHT)//2))
            bettext = FONT.render('BET', True, BUTTON_TEXT_COLOR)
            screen.blit(bettext, (MIDW-44, (MIDH+HEIGHT)//2-18))
            reset = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(MIDW-100, MIDH//4))
            resettext = FONT_SMALL.render('RESET', True, BUTTON_TEXT_COLOR)
            screen.blit(resettext, (MIDW-130, MIDH//4-8))
            start = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(MIDW+100, MIDH//4))
            starttext = FONT_SMALL.render('START', True, BUTTON_TEXT_COLOR)
            screen.blit(starttext, (MIDW+70, MIDH//4-8))
            button_list.append(bet)
            button_list.append(reset)
            button_list.append(start)
        else:
            scoretext = FONT_SMALL.render(f'Score: {phand.score}', True, TEXT_COLOR)
            screen.blit(scoretext, (10, HEIGHT-30))
            hit = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(WIDTH//6, (MIDH+3*HEIGHT)//4))
            hittext = FONT_SMALL.render('HIT', True, BUTTON_TEXT_COLOR)
            screen.blit(hittext, (WIDTH//6-15, (MIDH+3*HEIGHT)//4-8))
            stand = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(5*WIDTH//6, (MIDH+3*HEIGHT)//4))
            standtext = FONT_SMALL.render('STAND', True, BUTTON_TEXT_COLOR)
            screen.blit(standtext, (5*WIDTH//6-30, (MIDH+3*HEIGHT)//4-8))
            button_list.append(hit)
            button_list.append(stand)
    return button_list



def play():
    run = True
    while run:
        timer.tick(FPS)
        screen.fill(BG_COLOR)
        global playing
        global betting
        button_list = drawgame(playing, betting)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONUP:
                if not playing:
                    if button_list[0].collidepoint(event.pos):
                        betting = True
                        playing = True
                        button_list = drawgame(playing, betting)
                if playing and betting:
                    if button_list[0].collidepoint(event.pos):
                        BetAdd()
                    if button_list[1].collidepoint(event.pos):
                        BetReset()
                    if button_list[2].collidepoint(event.pos):
                        betting = False
                        button_list = drawgame(playing, betting)
                if playing and not betting:
                    if button_list[0].collidepoint(event.pos):
                        simulatecard(MIDW, MIDH-52, deck.draw())
                

        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    play()