import pygame
import random
import CONFIG


pygame.init()
screen = pygame.display.set_mode(CONFIG.SCREEN.size)
clock = pygame.time.Clock()

import Actions, music, Sprites

FPS = 200
i = 0
v = 20
left = False
right = False
up = False

sprites = pygame.sprite.Group()
hero = Sprites.Player(CONFIG.SCREEN.size)
sprites.add(hero)

running = True
while running:

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DELETE:
            running = False
        
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
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
            music.menusound.play(-1)
        screen.fill((0, 0, 0))
        Actions.maincaption(screen, CONFIG.SCREEN.size, 139)
        Actions.pressenter(screen, CONFIG.SCREEN.size, 139)
        CONFIG.menu = False
    
    # START GAME
    if CONFIG.startgame:
        CONFIG.fmenu = True
        music.menusound.stop()
        screen.fill((35, 35, 35))
        sprites.draw(screen)
        hero.update(left, right, up)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()