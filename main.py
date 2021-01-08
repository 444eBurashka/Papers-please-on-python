import pygame
import random
import CONFIG
import intro
import time


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(CONFIG.SCREEN.size)
menusound = pygame.mixer.Sound('Music/menu_soundtrack.mp3')
clock = pygame.time.Clock()

FPS = 60
i = 139
v = 40

intro.intro(screen, CONFIG.SCREEN.size)
menusound.play(-1)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                running = False
    
    
    
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()