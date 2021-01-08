import pygame
import random
import CONFIG
import Actions, music

pygame.init()
screen = pygame.display.set_mode(CONFIG.SCREEN.size)
clock = pygame.time.Clock()

FPS = 60
i = 0
v = 20

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                running = False
    
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
        screen.fill((0, 0, 0))
        Actions.maincaption(screen, CONFIG.SCREEN.size, 139)
        Actions.pressenter(screen, CONFIG.SCREEN.size, 139)
        CONFIG.menu = False
        

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()