import pygame as pg

pg.init()
WIDTH = 900
HEIGHT = 600
MIDW = WIDTH // 2
MIDH = HEIGHT // 2
screen = pg.display.set_mode([WIDTH, HEIGHT])
FPS = 60
FONT = pg.font.Font("freesansbold.ttf", 44)
FONT_SMALL = pg.font.Font("freesansbold.ttf", 18)
timer = pg.time.Clock()
playing = False
betting = True
BG_COLOR = "#00A000"
BUTTON_COLOR = '#FF0000'
BUTTON_TEXT_COLOR = '#FFFFFF'
TEXT_COLOR = '#FFFFFF'

def simulatecard(xpos, ypos, card):
    xpos = xpos - 33
    ypos = ypos - 48
    if card.revealed:
        card_img = pg.image.load(f"Card_designs\{card.name}.png")
    else:
        card_img = pg.image.load("Card_designs\Back_card.png")
    screen.blit(card_img, (xpos, ypos))