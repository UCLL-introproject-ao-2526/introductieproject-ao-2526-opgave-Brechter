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
tracks = ["Tracks/smooth-evening-saxophone-jazz-background-music-for-youtube-345557.mp3", 
          "Tracks/smooth-instrumental-jazz-music-360498.mp3", 
          "Tracks/smooth-jazz-388604.mp3",
          "Tracks/smooth-jazz-cafe-session-1-306314.mp3",
          "Tracks/smooth-jazz-saxophone-solo-with-a-lofi-vibe-253950.mp3",
          "Tracks/background-jazz-golden-whisper-358520.mp3",
          "Tracks/jazz-cafe-background-348913.mp3",
          "Tracks/jazz-lounge-relaxing-background-music-412597.mp3",
          "Tracks/night-jazz-beats-10039.mp3",
          "Tracks/relax-jazz-velvet-rain-357852.mp3",
          "Tracks/royalty-free-jazz-coastal-melody-363473.mp3",
          "Tracks/smooth-coffee-254076.mp3"]
coins_in_anim = []
coinxs = []

#colors
BG_COLOR = "#00A000"
BUTTON_COLOR = '#FF322E'
BUTTON_TEXT_COLOR = '#FFFFFF'
TEXT_COLOR = '#FFFFFF'
WIN_COLOR = "#E9E10D"
LOSE_COLOR = '#FF322E'
TIED_COLOR = "#4040FF"
DEAD_COLOR = "#000000"

#gamestates and conditions
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
music_on = True
coinanimation = False
music_allowed = True

    #here are some functions that don't really involve a specific part of the game functionality

#more about this function in logboek.md under Beta 1.1
#it works for position configurations of 6421357, this function caps at 7 because it's used for this game.
#to expand it you'll need to handle even numbers on a case-by-case basis.
#though you could do something by multiplying bools with lists and adding it to l1 and lf.
def add_to_list(elem, list):
    list.append(elem)
    if len(list)%2 == 1:
        return list
    else:
        list.reverse()
        if len(list) == 2:
            return list
        else:
            l1 = [list[-3], list[-1]]
            lf = [list[0], list[2]]
            if len(list) == 4:
                return l1 + lf
            else:
                return l1 + [list[1], list[4]] + lf

#this function generates the rules tab
def ruleswritten(screen):
    with open('Project/Rules.txt', 'r') as file:
        lines = file.readlines()
        ycoord = 10
        for line in lines:
            line.strip()
            if line[0] == "=":
                text = FONT_SMALL.render(line[1:-1], True, TEXT_COLOR)
                ycoord += 30
            else:
                text = FONT_TINY.render(line[:-1], True, TEXT_COLOR)
                ycoord += 20
            center = text.get_rect(center = (MIDW, ycoord))
            screen.blit(text, center)