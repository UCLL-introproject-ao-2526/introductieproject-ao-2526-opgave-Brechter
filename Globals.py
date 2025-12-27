import pygame as pg

#initiate
pg.init()

#coördinates
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
FPS = 60

#objects
screen = pg.display.set_mode([WIDTH, HEIGHT])
FONT = pg.font.Font("freesansbold.ttf", 44)
FONT_SMALL = pg.font.Font("freesansbold.ttf", 18)
FONT_TINY = pg.font.Font("freesansbold.ttf", 14)
FONT_BIG = pg.font.Font("freesansbold.ttf", 100)
timer = pg.time.Clock()

#colors
BG_COLOR = "#00A000"
BUTTON_COLOR = '#FF0000'
BUTTON_TEXT_COLOR = '#FFFFFF'
TEXT_COLOR = '#FFFFFF'
WIN_COLOR = "#E9E10D"
LOSE_COLOR = "#FF0000"
TIED_COLOR = "#4040FF"
DEAD_COLOR = "#000000"

#gamestates
playing = False
betting = True
dealerturn_init = False
dealerturn = False
game_end = False
insurask = False
insur = False
winscreen = False
losescreen = False
tiedscreen = False
deadscreen = False
game_end = False
playerdead = False
setupanimation = False
ingame = False
pcardanimation = False
dcardanimation = False
prevent_bet = False
cheats_on = False
show_rules = False
blackjack = False
