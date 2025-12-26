import pygame as pg

pg.init()
WIDTH = 900
HEIGHT = 600
MIDW = WIDTH // 2
MIDH = HEIGHT // 2
DECK_POS_X = MIDW - 33
DECK_POS_Y = MIDH - 72
PHAND_POS_Y = MIDH + 150
DHAND_POS_Y = MIDH - 198
HAND_POS_X_ODD = [MIDW, MIDW-66, MIDW+66, MIDW-132, MIDW+132, MIDW-198, MIDW+198]
HAND_POS_X_EVEN = [MIDW+33, MIDW-33, MIDW+99, MIDW-99, MIDW+165, MIDW-165]
screen = pg.display.set_mode([WIDTH, HEIGHT])
FPS = 60
FONT = pg.font.Font("freesansbold.ttf", 44)
FONT_SMALL = pg.font.Font("freesansbold.ttf", 18)
FONT_BIG = pg.font.Font("freesansbold.ttf", 100)
timer = pg.time.Clock()
playing = False
betting = True
BG_COLOR = "#00A000"
BUTTON_COLOR = '#FF0000'
BUTTON_TEXT_COLOR = '#FFFFFF'
TEXT_COLOR = '#FFFFFF'
WIN_COLOR = "#E9E10D"
LOSE_COLOR = "#FF0000"
TIED_COLOR = "#4040FF"
dealerturn_init = False
dealerturn = False
game_end = False
insurask = False
insur = False
winscreen = False
losescreen = False
tiedscreen = False
game_end = False
playerdead = False
setupanimation = False
ingame = False



def simulatecard(xpos, ypos, card):
    xpos = xpos - 33
    ypos = ypos - 48
    if card.revealed:
        card_img = pg.image.load(f"Card_designs\{card.name}.png")
    else:
        card_img = pg.image.load("Card_designs\Back_card.png")
    screen.blit(card_img, (xpos, ypos))