import pygame as pg


pg.init()
WIDTH = 800
HEIGHT = 600
MIDW = WIDTH // 2
MIDH = HEIGHT // 2
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("Blackjack")
FPS = 60
#FONT = pg.font.Font("arial.ttf", 44)
timer = pg.time.Clock()

run = True
while run:
    timer.tick(FPS)
    screen.fill("#00A000")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
pg.quit()