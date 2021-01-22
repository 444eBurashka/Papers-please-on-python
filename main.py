import pygame
import random
import CONFIG
from datetime import datetime
from camera import *


pygame.init()
screen = pygame.display.set_mode(CONFIG.SCREEN.size)
clock = pygame.time.Clock()

import Actions, music, Sprites

smth_lst = [Sprites.Smth(CONFIG.SCREEN.size, 100 * _) for _ in range(1, 29)]
brikcs_lst = [Sprites.bricks(CONFIG.SCREEN.size, 517 * _, 1) for _ in range(6)]
gg1 = Sprites.gg1(CONFIG.SCREEN.size)
po = Sprites.PO(CONFIG.SCREEN.size)
puzzle_1 = Sprites.Puzzle1(CONFIG.SCREEN.size)
FPS = 200
i = 0
game_size = (3000, CONFIG.SCREEN.size[1])
v = 20
left = False
right = False
up = False
bg = pygame.Surface((CONFIG.SCREEN.size[0], CONFIG.SCREEN.size[1]))
bg.fill(pygame.Color(30, 30, 30))
sprites = pygame.sprite.Group()
hero = Sprites.Player(game_size)
for _ in smth_lst:
    sprites.add(_)
for _ in brikcs_lst:
    sprites.add(_)
sprites.add(po)
sprites.add(puzzle_1)
sprites.add(gg1)
sprites.add(hero)
camera = Camera(camera_configure, game_size, CONFIG.SCREEN.size) 
can_click_enter = False

starttime = datetime.now()

finish_key_1 = False
finish_key_2 = False
finish_key_3 = False

running = True
while running:

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DELETE:
            running = False
        
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN and can_click_enter:
            if CONFIG.finish_enter:
                CONFIG.menu = True
                CONFIG.finishgame_menu = False
            else:
                CONFIG.menu = False
                CONFIG.startgame = True
        
        elif CONFIG.startgame:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                CONFIG.startgame = False
                CONFIG.menu = True
            elif e.type == pygame.KEYDOWN and (e.key == pygame.K_w or e.key == pygame.K_UP):
                up = True
            elif e.type == pygame.KEYDOWN and (e.key == pygame.K_a or e.key == pygame.K_LEFT):
                left = True
            elif e.type == pygame.KEYDOWN and (e.key == pygame.K_d or e.key == pygame.K_RIGHT):
                right = True
            elif e.type == pygame.KEYUP and (e.key == pygame.K_w or e.key == pygame.K_UP):
                up = False
            elif e.type == pygame.KEYUP and (e.key == pygame.K_a or e.key == pygame.K_LEFT):
                left = False
            elif e.type == pygame.KEYUP and (e.key == pygame.K_d or e.key == pygame.K_RIGHT):
                right = False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_o:
                d = [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0]
                for i in range(len(smth_lst)):
                    if d[i]:
                        smth_lst[i].change()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_e:
                gg1.change()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_c:
                finish_key_1 = True
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_1:
                finish_key_2 = True
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_4:
                finish_key_3 = True
            elif e.type == pygame.KEYUP and e.key == pygame.K_c:
                finish_key_1 = False
            elif e.type == pygame.KEYUP and e.key == pygame.K_1:
                finish_key_2 = False
            elif e.type == pygame.KEYUP and e.key == pygame.K_4:
                finish_key_3 = False
    
    # START INTRO
    if CONFIG.startintro_1:
        music.startintrosound.play()
        screen.fill((0, 0, 0))
        Actions.startintro(screen, CONFIG.SCREEN.size, i) 
        if i < 140:
            i += v / FPS
        if i >= 140:
            CONFIG.startintro_1 = False
            CONFIG.startintro_2 = True
    elif CONFIG.startintro_2:
        screen.fill((0, 0, 0))
        Actions.startintro(screen, CONFIG.SCREEN.size, i)
        if i > 0:
            i -= (v + 20) / FPS
        if i <= 3:
            CONFIG.startintro_2 = False
            CONFIG.startintro_3 = True
            i = 1
    elif CONFIG.startintro_3:
        music.startintrosound.stop()
        music.menusound.play(-1)
        can_click_enter = True
        screen.fill((0, 0, 0))
        if i < 140:
            i += v / FPS
        Actions.maincaption(screen, CONFIG.SCREEN.size, i)
        if i >= 140:
            CONFIG.startintro_3 = False
            CONFIG.menu = True
    
    # MAIN MENU
    if CONFIG.menu:
        if CONFIG.fmenu:
            music.start_game.stop()
            music.menusound.play(-1)
        screen.fill((0, 0, 0))
        Actions.maincaption(screen, CONFIG.SCREEN.size, 139)
        Actions.pressenter(screen, CONFIG.SCREEN.size, 139)
        CONFIG.menu = False
        CONFIG.finish_enter = False

    # START GAME
    if CONFIG.startgame:
        if CONFIG.time:
            starttime = datetime.now()
            CONFIG.time = False
        CONFIG.fmenu = True
        music.menusound.stop()
        if CONFIG.scream1:
            music.scream1.play()
            CONFIG.scream1 = False
        else:
            music.start_game.set_volume(10)
            music.start_game.play(-1)
        screen.fill((35, 35, 35))
        sprites.draw(screen)
        screen.blit(bg, (0,0))
        camera.update(hero)
        hero.update(left, right, up)
        for sprite in sprites:
            screen.blit(sprite.image, camera.apply(sprite))
        
        if finish_key_1 == finish_key_2 == finish_key_3 == True:
            CONFIG.finishgame = True
            CONFIG.startgame = False
            i = 0
    
    # FINISH GAME
    if CONFIG.finishgame:
        music.start_game.stop()
        music.menusound.play(-1)
        screen.fill((0, 0, 0))
        if i < 140:
            i += v / FPS
        d = datetime.now() - starttime
        Actions.finalcaption(screen, CONFIG.SCREEN.size, i, d)
        if i >= 140:
            CONFIG.finishgame = False
            CONFIG.finishgame_menu = True
    
    if CONFIG.finishgame_menu:
        screen.fill((0, 0, 0))
        Actions.finalcaption(screen, CONFIG.SCREEN.size, 139, d)
        Actions.pressenter(screen, CONFIG.SCREEN.size, 139)
        CONFIG.finishgame_menu = False
        CONFIG.finish_enter = True
        finish_key_1 = finish_key_2 = finish_key_3 = False

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()