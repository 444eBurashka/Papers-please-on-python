import pygame
import random
import CONFIG
import intro, music

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
        intro.startintro(screen, CONFIG.SCREEN.size, i) 
        if i < 140:
            i += v / FPS
        if i >= 140:
            CONFIG.startintro_1 = False
            CONFIG.startintro_2 = True
    elif CONFIG.startintro_2:
        intro.startintro(screen, CONFIG.SCREEN.size, i) 
        if i > 0:
            i -= (v + 20) / FPS
        if i <= 3:
            CONFIG.startintro_2 = False
            CONFIG.startintro_3 = True
            i = 1
    elif CONFIG.startintro_3:
        music.startintrosound.stop()
        music.menusound.play(-1)
        intro.maincaption(screen, CONFIG.SCREEN.size, i)
        CONFIG.startintro_3 = False
        CONFIG.menu = True
    
    # MAIN MENU
    if CONFIG.menu:
        width, height = CONFIG.SCREEN.size
        font = pygame.font.Font('Fonts/17238.otf', 20)
        text = font.render("Нажмите Enter чтобы продолжить...", True, (139, 0, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2 + 100
        screen.blit(text, (text_x, text_y))
        CONFIG.menu = False

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()