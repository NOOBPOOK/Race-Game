import random
from random import seed
import numpy
import pygame
import time
import sys
import pygame.locals
from pygame import KEYDOWN, K_ESCAPE, K_UP, K_SPACE, K_DOWN, QUIT, K_5, K_6, K_4, K_3, K_2, K_1, K_LEFT, K_RIGHT

FPS = 60
SCREENHEIGHT = 541
SCREENWIDTH = 600
pygame.mixer.init()
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYERY = 403
PLAYERX = 265


def welcome():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and (event.key == K_DOWN or event.key == K_ESCAPE):
                print("Game Ended!")
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_UP or event.key == K_SPACE):
                return
            else:
                SCREEN.blit(GAME_SPRITES['welcome'], (0, 0))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def choose():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == K_DOWN and event.key == K_ESCAPE):
                print("Game Ended!")
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_1:
                GAME_SPRITES['selectcars'] = GAME_SPRITES['selectcars'][0]
                GAME_SOUNDS['unlock'].play()
                return
            elif event.type == KEYDOWN and event.key == K_2:
                GAME_SPRITES['selectcars'] = GAME_SPRITES['selectcars'][1]
                GAME_SOUNDS['unlock'].play()
                return
            elif event.type == KEYDOWN and event.key == K_3:
                GAME_SPRITES['selectcars'] = GAME_SPRITES['selectcars'][2]
                GAME_SOUNDS['unlock'].play()
                return
            elif event.type == KEYDOWN and event.key == K_4:
                GAME_SPRITES['selectcars'] = GAME_SPRITES['selectcars'][3]
                GAME_SOUNDS['unlock'].play()
                return
            elif event.type == KEYDOWN and event.key == K_5:
                GAME_SPRITES['selectcars'] = GAME_SPRITES['selectcars'][3]
                GAME_SOUNDS['unlock'].play()
                return
            elif event.type == KEYDOWN and event.key == K_6:
                print("Cannot choose that car!")
            else:
                SCREEN.blit(GAME_SPRITES['choose'], (0, 0))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def maingame():
    global k_1, k_2, k_3, k_4, k_5
    score = 0
    playerx = PLAYERX
    playery = PLAYERY
    speed = 4
    lane1 = [{'x': 30, 'y': random.randint(-1000, 0)}]
    lane2 = [{'x': 140, 'y': random.randint(-1000, -300)}]
    lane3 = [{'x': 260, 'y': random.randint(-1000, -700)}]
    lane4 = [{'x': 380, 'y': random.randint(-1000, -100)}]
    lane5 = [{'x': 495, 'y': random.randint(-1000, -50)}]
    list_d = [0, 1, 2, 3]
    k_1 = random.choice(list_d)
    k_2 = random.choice(list_d)
    k_3 = random.choice(list_d)
    k_4 = random.choice(list_d)
    k_5 = random.choice(list_d)
    GAME_SOUNDS['racecar'].set_volume(0.1)
    GAME_SOUNDS['racecar'].play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                print("Game Ended!")
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_LEFT:
                playerx -= 30
                if playerx < 25:
                    playerx = 25
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                playerx += 30
                if playerx > 500:
                    playerx = 500

        # check if collide!
        collide(playerx, playery, lane1, lane2, lane3, lane4, lane5, score)

        # Move Cars down!
        for lane_1, lane_2, lane_3, lane_4, lane_5 in zip(lane1, lane2, lane3, lane4, lane5):
            lane_1['y'] += speed
            lane_2['y'] += speed
            lane_3['y'] += speed
            lane_4['y'] += speed
            lane_5['y'] += speed

        # add points
        score += 1

        #CHECK LEVEL AND INCREASE SPEED
        if score/60 % 10 == 0:
            speed += 0.5
            print(speed)

        # add  cars when old car hits the half screen
        if lane1[0]['y'] >= 541:
            lan1 = {'x': 30, 'y': random.randint(-1000, 0)}
            lane1.append(lan1)
        if lane2[0]['y'] >= 541:
            lan2 = {'x': 140, 'y': random.randint(-1000, -400)}
            lane2.append(lan2)
        if lane3[0]['y'] >= 541:
            lan3 = {'x': 260, 'y': random.randint(-1000, -250)}
            lane3.append(lan3)
        if lane4[0]['y'] >= 541:
            lan4 = {'x': 380, 'y': random.randint(-1000, -100)}
            lane4.append(lan4)
        if lane5[0]['y'] >= 541:
            lan5 = {'x': 495, 'y': random.randint(-1000, -255)}
            lane5.append(lan5)

        # remove down cars!
        if lane1[0]['y'] >= 541:
            lane1.pop(0)
        if lane2[0]['y'] >= 541:
            lane2.pop(0)
        if lane3[0]['y'] >= 541:
            lane3.pop(0)
        if lane4[0]['y'] >= 541:
            lane4.pop(0)
        if lane5[0]['y'] >= 541:
            lane5.pop(0)

        #make side swoosh sounds
        #for lane1
        if 350 <= lane2[0]['y'] + 130 and 0 < playerx < 120:
            GAME_SOUNDS['swoosh'].set_volume(0.2)
            GAME_SOUNDS['swoosh'].play()
        #for lane2
        if (350 <= lane1[0]['y'] or playery <= lane3[0]['y']) and 120 < playerx < 240:
            GAME_SOUNDS['swoosh'].set_volume(0.2)
            GAME_SOUNDS['swoosh'].play()
        #for lane3
        if (350 <= lane2[0]['y'] or playery <= lane4[0]['y']) and 240 < playerx < 360:
            GAME_SOUNDS['swoosh'].set_volume(0.2)
            GAME_SOUNDS['swoosh'].play()
        #for lane4
        if (350 <= lane3[0]['y'] or playery <= lane5[0]['y']) and 360 < playerx < 480:
            GAME_SOUNDS['swoosh'].set_volume(0.2)
            GAME_SOUNDS['swoosh'].play()
        #for lane5
        if 350 <= lane4[0]['y'] and 480 < playerx < 600:
            GAME_SOUNDS['swoosh'].set_volume(0.2)
            GAME_SOUNDS['swoosh'].play()

        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        SCREEN.blit(GAME_SPRITES['selectcars'], (playerx, playery))
        SCREEN.blit(GAME_SPRITES['runcars'][k_1], (lane1[0]['x'], lane1[0]['y']))
        SCREEN.blit(GAME_SPRITES['runcars'][k_2], (lane2[0]['x'], lane2[0]['y']))
        SCREEN.blit(GAME_SPRITES['runcars'][k_3], (lane3[0]['x'], lane3[0]['y']))
        SCREEN.blit(GAME_SPRITES['runcars'][k_4], (lane4[0]['x'], lane4[0]['y']))
        SCREEN.blit(GAME_SPRITES['runcars'][k_5], (lane5[0]['x'], lane5[0]['y']))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def collide(playerx, playery, lane1, lane2, lane3, lane4, lane5, score):
    if playery <= lane1[0]['y'] + 130 <= 540 and (20 <= playerx <= 80):
        coly = lane1[0]['y'] + 70
        colx = playerx - 60
        collision(playerx, playery, lane1, lane2, lane3, lane4, lane5, score, colx, coly)

    elif playery <= lane2[0]['y'] + 130 <= 540 and (145 <= playerx <= 200 or 145 <= playerx+65 <= 200):
        coly = lane2[0]['y'] + 70
        if 145 <= playerx <= 200:
            colx = playerx - 60
        else:
            colx = playerx + 15
        collision(playerx, playery, lane1, lane2, lane3, lane4, lane5, score, colx, coly)

    elif playery <= lane3[0]['y'] + 130 <= 540 and (265 <= playerx <= 320 or 265 <= playerx+65 <= 320):
        coly = lane3[0]['y'] + 70
        if 265 <= playerx <= 320:
            colx = playerx - 60
        else:
            colx = playerx + 15
        collision(playerx, playery, lane1, lane2, lane3, lane4, lane5, score, colx, coly)

    elif playery <= lane4[0]['y'] + 130 <= 540 and (385 <= playerx <= 440 or 385 <= playerx+65 <= 440):
        coly = lane4[0]['y'] + 70
        if 385 <= playerx <= 440:
            colx = playerx - 60
        else:
            colx = playerx + 15
        collision(playerx, playery, lane1, lane2, lane3, lane4, lane5, score, colx, coly)

    elif playery <= lane5[0]['y'] + 130 <= 540 and (495 <= playerx+65 <= 570):
        coly = lane5[0]['y'] + 70
        colx = playerx + 10
        collision(playerx, playery, lane1, lane2, lane3, lane4, lane5, score, colx, coly)

def collision(playerx, playery, lane1, lane2, lane3, lane4, lane5, score, colx, coly):
    global k_1, k_2, k_3, k_4, k_5
    GAME_SOUNDS['racecar'].stop()
    GAME_SOUNDS['bomb'].set_volume(0.2)
    GAME_SOUNDS['bomb'].play()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_ESCAPE):
                pygame.quit()
                print(f"***You covered a distance of {int(score / 60)}***")
                sys.exit()
            if event.type == QUIT:
                pygame.quit()
                print(f"***Your covered a distance of {int(score / 60)}***")
                sys.exit()

        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        SCREEN.blit(GAME_SPRITES['selectcars'], (playerx, playery))
        SCREEN.blit(GAME_SPRITES['runcars'][k_1], (lane1[0]['x'], lane1[0]['y']))
        SCREEN.blit(GAME_SPRITES['runcars'][k_2], (lane2[0]['x'], lane2[0]['y']))
        SCREEN.blit(GAME_SPRITES['runcars'][k_3], (lane3[0]['x'], lane3[0]['y']))
        SCREEN.blit(GAME_SPRITES['runcars'][k_4], (lane4[0]['x'], lane4[0]['y']))
        SCREEN.blit(GAME_SPRITES['runcars'][k_5], (lane5[0]['x'], lane5[0]['y']))
        SCREEN.blit(GAME_SPRITES['boom'], (colx, coly))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    pygame.init()  # Intialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("RACE GAME by NOOBPOOK")
    GAME_SPRITES['background'] = pygame.image.load('Graphics/background.png').convert_alpha()
    GAME_SPRITES['welcome'] = pygame.image.load('Graphics/welcome.png').convert_alpha()
    GAME_SPRITES['boom'] = pygame.image.load('Graphics/boom.png').convert_alpha()
    GAME_SPRITES['choose'] = pygame.image.load('Graphics/choose.png').convert_alpha()
    GAME_SPRITES['selectcars'] = (
        pygame.image.load('Graphics/Select1.png').convert_alpha(),
        pygame.image.load('Graphics/Select2.png').convert_alpha(),
        pygame.image.load('Graphics/Select3.png').convert_alpha(),
        pygame.image.load('Graphics/Select4.png').convert_alpha(),
        pygame.image.load('Graphics/Select5.png').convert_alpha(),
        pygame.image.load('Graphics/Select6.png').convert_alpha()
    )
    GAME_SPRITES['runcars'] = (
        pygame.image.load('Graphics/Run1.png').convert_alpha(),
        pygame.image.load('Graphics/Run2.png').convert_alpha(),
        pygame.image.load('Graphics/Run3.png').convert_alpha(),
        pygame.image.load('Graphics/Run4.png').convert_alpha(),
        pygame.image.load('Graphics/Run5.png').convert_alpha(),
    )
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('Music/Swoosh.wav')
    GAME_SOUNDS['racecar'] = pygame.mixer.Sound('Music/engine_const.wav')
    GAME_SOUNDS['unlock'] = pygame.mixer.Sound('Music/unlock.wav')
    GAME_SOUNDS['bomb'] = pygame.mixer.Sound('Music/explosion.wav')

    welcome()
    choose()
    maingame()

