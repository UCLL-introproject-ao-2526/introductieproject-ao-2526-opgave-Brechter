import pygame as pg
import random as rd
from Wallet import *
from Cards import *
from Pointsystem import *
from Setup import *


#intialising
pg.init()
pg.display.set_caption("Blackjack")
from Globals import *


def dealerplay(dealerhand):
    global dealerturn
    global game_end
    global dcardanimation
    if 0 <= dealerhand.score < 17:
        dealerhand.retrieve()
        dcardanimation = True
        game_end = False
        dealerturn = True

def drawcards(phand, dhand, plinvis=False, dlinvis=False):
        if len(phand.cards) > 0:
            plen = len(phand.cards)
            pxpos = HAND_POS_X_EVEN if plen%2 == 0 else HAND_POS_X_ODD
            if plen%2==1:
                for i in range(plen - 1):
                    simulatecard(pxpos[i], PHAND_POS_Y, phand.cards[i])
                if not plinvis:
                    simulatecard(pxpos[plen - 1], PHAND_POS_Y, phand.cards[plen - 1])
            else:
                for i in range(plen):
                    if i != plen-2:
                        simulatecard(pxpos[i], PHAND_POS_Y, phand.cards[i])
                if not plinvis:
                    simulatecard(pxpos[plen - 2], PHAND_POS_Y, phand.cards[plen - 2])
        
        if len(dhand.cards) > 0:    
            dlen = len(dhand.cards)
            dxpos = HAND_POS_X_EVEN if dlen %2 == 0 else HAND_POS_X_ODD
            if dlen%2 == 1:
                for j in range(dlen - 1):
                    simulatecard(dxpos[j], DHAND_POS_Y, dhand.cards[j])
                if not dlinvis:
                    simulatecard(dxpos[dlen - 1], DHAND_POS_Y, dhand.cards[dlen - 1])
            else:
                for i in range(dlen):
                    if i != dlen-2:
                        simulatecard(dxpos[i], DHAND_POS_Y, dhand.cards[i])
                if not dlinvis:
                    simulatecard(dxpos[dlen - 2], DHAND_POS_Y, dhand.cards[dlen - 2])
        

def drawgame(active, betting):
    
    #getting globals and making variables
    global winscreen
    global losescreen
    global tiedscreen  
    global insurask
    global insur
    global dealerturn
    global setupanimation
    global ingame
    global dcardanimation
    global pcardanimation
    global prevent_bet
    global cheats_on
    global blackjack
    global show_rules
    global music_on
    global coinanimation
    global coins_in_anim
    global coinxs
    button_list = []

    
    
    Music_button = pg.draw.rect(screen, BG_COLOR, (WIDTH-59, HEIGHT-44, 51, 36))
    
    #startscreen
    if show_rules:
        back = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(50, 50))
        backtext = FONT_SMALL.render('BACK', True, BUTTON_TEXT_COLOR)
        backcenter = backtext.get_rect(center=(50, 50))
        screen.blit(backtext, backcenter)
        button_list.append(back)
        ruleswritten(screen)
    elif not active:
        pg.draw.ellipse(screen, '#FFFFFF', (MIDW-148, MIDH//2-73, 296, 146))
        logo = pg.image.load('Card_designs/logo.png')
        logocenter = logo.get_rect(center = (MIDW, MIDH//2))
        screen.blit(logo, logocenter)
        play = pg.draw.circle(screen, color=BUTTON_COLOR, radius=75, center=(MIDW, 5*HEIGHT//8))
        playtext = FONT.render('PLAY', True, BUTTON_TEXT_COLOR)
        screen.blit(playtext, (MIDW-56, 5*HEIGHT//8-18))
        button_list.append(play)
        if not cheats_on:
            cheats = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(WIDTH-50, 50))
            cheatsignal = FONT_TINY.render('OFF', True, BUTTON_TEXT_COLOR)
            screen.blit(cheatsignal, (WIDTH-65, 52))
        else:
            cheats = pg.draw.circle(screen, color=TIED_COLOR, radius=40, center=(WIDTH-50, 50))
            cheatsignal = FONT_TINY.render('ON', True, BUTTON_TEXT_COLOR)
            screen.blit(cheatsignal, (WIDTH-62, 52))
        cheattext = FONT_TINY.render('CHEATS', True, BUTTON_TEXT_COLOR)
        screen.blit(cheattext, (WIDTH-78, 35))
        button_list.append(cheats)
        rules = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(50, 50))
        ruletext = FONT_SMALL.render('RULES', True, BUTTON_TEXT_COLOR)
        rulecenter = ruletext.get_rect(center=(50, 50))
        screen.blit(ruletext, rulecenter)
        button_list.append(rules)

    
    #once the game starts, you go to the betting menu
    else:

        #setting up the standard text during the game
        wallettext = FONT_SMALL.render(f'{wallet.amount}', True, TEXT_COLOR)
        screen.blit(wallettext, (33, 8))
        money_img = pg.image.load("Card_designs/Money.png")
        screen.blit(money_img, (8, 8))
        betamounttext = FONT_SMALL.render(f'{table.amount}', True, TEXT_COLOR) 
        screen.blit(betamounttext, (35, 50))
        bet_img = pg.image.load("Card_designs/Money_Bet.png")
        screen.blit(bet_img, (8, 45))
        if insur:
            ins_img = pg.image.load("Card_designs/Insurance.png")
            screen.blit(ins_img, (8, 75))
            insurancetext = FONT_SMALL.render(f'{insurance.amount}', True, TEXT_COLOR) 
            screen.blit(insurancetext, (35, 80))
        if cheats_on:
            countimg = pg.image.load("Card_designs/count.png")
            cimgtr = countimg.get_rect(topright=(WIDTH-8, 8))
            screen.blit(countimg, cimgtr)
            cardcounttext = FONT_SMALL.render(f"{deck.count}", True, TEXT_COLOR)
            block = cardcounttext.get_rect(topright=(WIDTH-35, 10))
            screen.blit(cardcounttext, block)

        #the betting menu
        if betting:
            if coinanimation:
                for i in range(len(coins_in_anim)):
                    coins_in_anim[i] = Coinanimation(screen, coins_in_anim[i])
                while i < len(coins_in_anim):
                    if coins_in_anim[i][1] > 15:
                        coins_in_anim.pop(i)
                        i -= 1
                    i += 1
                coinanimation = len(coins_in_anim) > 0
            
            bet = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(MIDW, MIDH))
            bettext = FONT_SMALL.render('BET', True, BUTTON_TEXT_COLOR)
            screen.blit(bettext, (MIDW-18, MIDH-9))

            reset = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(MIDW-100, MIDH))
            resettext = FONT_SMALL.render('RESET', True, BUTTON_TEXT_COLOR)
            screen.blit(resettext, (MIDW-130, MIDH-9))

            start = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(MIDW+100, MIDH))
            starttext = FONT_SMALL.render('START', True, BUTTON_TEXT_COLOR)
            screen.blit(starttext, (MIDW+70, MIDH-9))

            back = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(MIDW, HEIGHT-50))
            gobacktext = FONT_TINY.render('BACK', True, BUTTON_TEXT_COLOR)
            tomenutext = FONT_TINY.render('TO MENU', True, BUTTON_TEXT_COLOR)
            gbtcenter = gobacktext.get_rect(center = (MIDW, HEIGHT-60))
            tomenucenter = tomenutext.get_rect(center = (MIDW, HEIGHT-42))
            screen.blit(gobacktext, gbtcenter)
            screen.blit(tomenutext, tomenucenter)

            button_list.append(bet)
            button_list.append(reset)
            button_list.append(start)
            button_list.append(back)

            if prevent_bet:
                text = FONT_SMALL.render('You must place a bet before playing', True, BUTTON_TEXT_COLOR)
                screen.blit(text, (292, MIDH+75))

            

        
        #if the game ends
        elif winscreen:
            screen.fill(WIN_COLOR)
            endtext = FONT_BIG.render('YOU WON', True, TEXT_COLOR)
            if blackjack:
                blackjacktext = FONT.render("BLACKJACK!", True, TEXT_COLOR)
                midbjt = blackjacktext.get_rect(center = (MIDW, MIDH+30))
                etmid = endtext.get_rect(center = (MIDW, MIDH-30))
                screen.blit(endtext, etmid)
                screen.blit(blackjacktext, midbjt)
            else:
                etmid = endtext.get_rect(center = (MIDW, MIDH))
                screen.blit(endtext, etmid)
            for i in range(len(coins_in_anim)):
                coins_in_anim[i] = Coinanimation(screen, coins_in_anim[i], x=coinxs[i], y=MIDH-(21+blackjack*30))
            while i < len(coins_in_anim):
                if coins_in_anim[i][1] > 15:
                    coins_in_anim.pop(i)
                    coinxs.pop(i)
                    i -= 1
                i += 1
            coinanimation = len(coins_in_anim) > 0
        elif losescreen:
            screen.fill(LOSE_COLOR)
            endtext = FONT_BIG.render('YOU LOST', True, TEXT_COLOR)    
            etmid = endtext.get_rect(center = (MIDW, MIDH))
            screen.blit(endtext, etmid)
        elif tiedscreen:
            screen.fill(TIED_COLOR)
            endtext = FONT_BIG.render("IT'S A TIE", True, TEXT_COLOR)  
            if blackjack:
                blackjacktext = FONT.render("BUT A BLACKJACK TIE", True, TEXT_COLOR)
                etmid = endtext.get_rect(center = (MIDW, MIDH-30))
                midbjt = blackjacktext.get_rect(center = (MIDW, MIDH+30))
                screen.blit(endtext, etmid)
                screen.blit(blackjacktext, midbjt)
            else:
                etmid = endtext.get_rect(center = (MIDW, MIDH))
                screen.blit(endtext, etmid)
        elif deadscreen:
            screen.fill(DEAD_COLOR)
            endtext = FONT_BIG.render("GAME OVER", True, LOSE_COLOR)
            etmid = endtext.get_rect(center = (MIDW, MIDH))
            screen.blit(endtext, etmid)

        #during the game itself
        else:
            deckimg = pg.image.load("Card_designs/Back_card.png")
            screen.blit(deckimg, (DECK_POS_X, DECK_POS_Y))
            if pcardanimation:
                drawcards(phand, dhand, True)
            elif dcardanimation:
                drawcards(phand, dhand, False, True)
            else:
                drawcards(phand, dhand)
            if not setupanimation:
                if phand.score != 100:
                    pscoretext = FONT_SMALL.render(f'Your score: {phand.score if phand.score >= 0 else "Dead"}', True, TEXT_COLOR)
                else:
                    pscoretext = FONT_SMALL.render(f'Your score: Winner! (7 cards)', True, TEXT_COLOR)
                if ingame:
                    dscoretext = FONT_SMALL.render(f"Dealer's score: ?", True, TEXT_COLOR)
                elif dhand.score != 100:
                    dscoretext = FONT_SMALL.render(f"Dealer's score: {dhand.score if dhand.score != -1 else "Dead"}", True, TEXT_COLOR)
                else:
                    dscoretext = FONT_SMALL.render(f"Dealer's score: Winner! (7 cards)", True, TEXT_COLOR)
                screen.blit(pscoretext, (8, HEIGHT-45))
                screen.blit(dscoretext, (8, HEIGHT-25))
                if ingame:
                    hit = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(WIDTH//6, PHAND_POS_Y))
                    hittext = FONT_SMALL.render('HIT', True, BUTTON_TEXT_COLOR)
                    screen.blit(hittext, (WIDTH//6-15, PHAND_POS_Y-9))
                    stand = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(5*WIDTH//6, PHAND_POS_Y))
                    standtext = FONT_SMALL.render('STAND', True, BUTTON_TEXT_COLOR)
                    screen.blit(standtext, (5*WIDTH//6-30, PHAND_POS_Y-9))
                    if not pcardanimation:
                        button_list.append(hit)
                        button_list.append(stand)
                    

                    #if the first card is an ace the player will be asked to buy insurance, if the dealer gets a blackjack, the player will get double the insurance back
                    if insurask and wallet.amount >= table.amount//2:
                        ins_y = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(50, MIDH))
                        ins_n = pg.draw.circle(screen, color=BUTTON_COLOR, radius=40, center=(WIDTH//6, MIDH))
                        yestext = FONT_SMALL.render('YES', True, BUTTON_TEXT_COLOR)
                        notext = FONT_SMALL.render('NO', True, BUTTON_TEXT_COLOR)
                        screen.blit(yestext, (31, MIDH-9))
                        screen.blit(notext, (138, MIDH-9))
                        instext = FONT_SMALL.render('INSURANCE?', True, TEXT_COLOR)
                        screen.blit(instext, (40, MIDH-80))
                        button_list.append(ins_y)
                        button_list.append(ins_n)
                    if insur and coinanimation:
                        for i in range(len(coins_in_anim)):
                            coins_in_anim[i] = Coinanimation(screen, coins_in_anim[i], x=50)
                        while i < len(coins_in_anim):
                            if coins_in_anim[i][1] > 15:
                                coins_in_anim.pop(i)
                                i -= 1
                            i += 1
                        coinanimation = len(coins_in_anim) > 0
                    
    Music_button_img = pg.image.load(f"Card_designs/Music_{'on' if music_on else 'off'}.png")
    Mbbr = Music_button_img.get_rect(bottomright = (WIDTH-8, HEIGHT-8))
    screen.blit(Music_button_img, Mbbr)
    button_list.append(Music_button)
    return button_list


    

def play():
    #setting up
    run = True
    frame = 0
    setupdealt = 0
    end_music = True
    just_played = -1

    #main game loop
    while run:
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
        global deadscreen
        global insurask
        global insur
        global playerdead
        global phand
        global setupanimation
        global ingame
        global pcardanimation
        global dcardanimation
        global prevent_bet
        global cheats_on
        global blackjack
        global show_rules
        global music_on
        global coinanimation
        global coins_in_anim
        global coinxs
        animation = dcardanimation or pcardanimation or setupanimation
        endscreen = winscreen or tiedscreen or losescreen or deadscreen
        button_list = drawgame(playing, betting)
        end_music = not pg.mixer.music.get_busy()

        if end_music and not deadscreen:
            end_music = False
            track_number = rd.randint(0, len(tracks)-1)
            while track_number == just_played:
                track_number = rd.randint(0, 4)
            just_played = track_number
            pg.mixer.music.load(tracks[track_number])
            pg.mixer.music.play()
        
        if setupanimation and frame > 30:
            if setupdealt < 2:
                pcardanimation = True
            else:
                pcardanimation = False
                dcardanimation = True
            frame = 0
            setupdealt += 1
            insurask = setup(setupdealt)
            if setupdealt == 4:
                setupanimation = False
                ingame = True

        if pcardanimation or dcardanimation:
            if frame > 15:
                pcardanimation, dcardanimation = False, False
            else:
                cardanimation(phand, dhand, frame, pcardanimation)

        #to check if the player dies
        if ingame and phand.score == -1:
            playerdead = True
            ingame = False
            frame = 0
        
        #once the player dies they get one second before the dealer reveals his card
        if playerdead and frame > 60:
            dealerturn_init = True
            playerdead = False


        #if the player has 7 cards, the dealer automatically begins
        if len(phand.cards) == 7 and frame > 59 and not (dealerturn_init or dealerturn or game_end or endscreen):
            ingame = False
            frame = 0
            dealerturn_init = True

        #the dealer's turn begins with him flipping his card and every second he'll draw a new one until he decides to end the game
        if dealerturn_init and frame > 59:
            dhand.cards[0].reveal()
            deck.cardcountupdate(dhand.cards[0])
            frame = 0
            dealerturn_init = False
            dealerturn = True

        #now the dealer can start pulling cards
        if dealerturn and frame > 58:
            frame = 0
            game_end = True
            dealerturn = False
            dealerplay(dhand)

        #3 seconds after the game ends, the endscreen will appear
        if game_end and frame > 180:
            gamestate = CompareScores(phand.score, dhand.score)
            dblackjack = dhand.score == 21
            if phand.score == 21:
                blackjack = True
            if gamestate == 0:
                losescreen = True
            elif gamestate == 1:
                tiedscreen = True
            else:
                winscreen = True
            Payout(gamestate, dblackjack, insur)
            if wallet.amount < 20:
                losescreen = False
                deadscreen = True
                pg.mixer.music.unload()
                pg.mixer.music.load("Tracks/game-over-deep-male-voice-clip-352695.mp3")
                pg.mixer.music.play()
            frame = 0
            game_end = False

        #5 seconds after the endscreen a new game will begin
        if endscreen and frame > 300:
            frame = 0
            winscreen, tiedscreen, losescreen, insur, blackjack = False, False, False, False, False
            insurance.amount = 0
            dhand.empty()
            phand.empty()
            betting = True
            setupdealt = 0
            if deadscreen:
                run = False

        if winscreen and frame < 285:
            coins_in_anim.append((pg.image.load("Card_designs/Coin.png"), 0))
            coinxs.append(rd.randint(MIDW-250, MIDW+250))
            if blackjack:
                coins_in_anim.append((pg.image.load("Card_designs/Coin.png"), 0))
                coinxs.append(rd.randint(MIDW-250, MIDW+250))
            coinanimation = True




        #start of the for loop

        #checking clicks
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONUP:
                
                if button_list[-1].collidepoint(event.pos):
                    music_on = not music_on
                    pg.mixer.music.set_volume(100*music_on)

                #startscreen
                if show_rules:
                    if button_list[0].collidepoint(event.pos):
                        show_rules = False
                elif not playing:
                    if button_list[0].collidepoint(event.pos):
                        betting = True
                        playing = True
                        button_list = drawgame(playing, betting)
                    if button_list[1].collidepoint(event.pos):
                        cheats_on = not cheats_on
                    if button_list[2].collidepoint(event.pos):
                        show_rules = True
                    
                #betting stage
                elif playing and betting:
                    if button_list[0].collidepoint(event.pos):
                        prevent_bet = False
                        BetAdd()
                        if wallet.amount >= 20:
                            coinanimation = True
                            coins_in_anim.append((pg.image.load("Card_designs/Coin.png"), 0))
                    if button_list[1].collidepoint(event.pos):
                        BetReset()
                    if button_list[2].collidepoint(event.pos):
                        if table.amount == 0:
                            prevent_bet = True
                        else:
                            prevent_bet = False
                            game_end = False
                            betting = False
                            setupanimation = True
                    if button_list[3].collidepoint(event.pos):
                        playing = False
                        prevent_bet = False
                        BetReset()

                #now it's the player's turn
                elif playing and not betting and not endscreen:
                    if not playerdead and len(phand.cards) < 7 and not animation and not (dealerturn_init or dealerturn or game_end):
                        if button_list[0].collidepoint(event.pos) and frame > 15:
                            phand.retrieve()
                            pcardanimation = True
                            frame = 0
                            if insurask:
                                insurask = False
                        if button_list[1].collidepoint(event.pos):
                            dealerturn_init = True
                            ingame = False
                            frame = 0
                            dhand.cards[0].reveal()
                            if insurask:
                                insurask = False
                        if insurask:
                            if button_list[2].collidepoint(event.pos):
                                insurask = False
                                insur = Betinsurance()
                                if wallet.amount >= table.amount//2:
                                    coinanimation = True
                                    coins_in_anim.append((pg.image.load("Card_designs/Coin.png"), 0))
                            if button_list[3].collidepoint(event.pos):
                                insurask = False

                
    #end of loop   
        frame +=1
        pg.display.flip()
    pg.mixer.music.unload()
    pg.quit()


if __name__ == "__main__":
    play()