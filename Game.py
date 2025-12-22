import pygame as pg
from Gameplay import *
from Wallet import *

pg.init()
WIDTH = 900
HEIGHT = 600
MIDW = WIDTH // 2
MIDH = HEIGHT // 2
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("Blackjack")
FPS = 60
FONT = pg.font.Font("freesansbold.ttf", 44)
FONT_SMALL = pg.font.Font("freesansbold.ttf", 18)
timer = pg.time.Clock()
playing = True
betting = False
BG_COLOR = "#00A000"
BUTTON_COLOR = '#FF0000'
BUTTON_TEXT_COLOR = '#FFFFFF'
TEXT_COLOR = '#FFFFFF'


def drawgame(active, betting):
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
        if betting:
            bet = pg.draw.circle(screen, color=BUTTON_COLOR, radius=75, center=(MIDW, (MIDH+HEIGHT)//2))
            bettext = FONT.render('BET', True, BUTTON_TEXT_COLOR)
            screen.blit(bettext, (MIDW-44, (MIDH+HEIGHT)//2-18))
            reset = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(MIDW, MIDH//4))
            resettext = FONT_SMALL.render('RESET', True, BUTTON_TEXT_COLOR)
            screen.blit(resettext, (MIDW-30, MIDH//4-8))
            button_list.append(bet)
            button_list.append(reset)
        else:
            hit = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(WIDTH//6, (MIDH+3*HEIGHT)//4))
            hittext = FONT_SMALL.render('HIT', True, BUTTON_TEXT_COLOR)
            screen.blit(hittext, (WIDTH//6-15, (MIDH+3*HEIGHT)//4-8))
            stand = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(5*WIDTH//6, (MIDH+3*HEIGHT)//4))
            standtext = FONT_SMALL.render('STAND', True, BUTTON_TEXT_COLOR)
            screen.blit(standtext, (5*WIDTH//6-30, (MIDH+3*HEIGHT)//4-8))
            button_list.append(hit)
            button_list.append(stand)



def play():
    run = True
    while run:
        timer.tick(FPS)
        screen.fill(BG_COLOR)
        drawgame(playing, betting)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    play()