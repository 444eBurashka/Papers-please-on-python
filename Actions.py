import pygame


def startintro(surf, screensize, i):
    width, height = screensize
    font = pygame.font.Font('Fonts/16905.ttf', 50)
    text1 = font.render("STEEL Gaming present", True, (i, 0, 0))
    text_x = width // 2 - text1.get_width() // 2
    text_y = height // 2 - text1.get_height() // 2
    surf.blit(text1, (text_x, text_y))


def maincaption(surf, screensize, i):
    width, height = screensize
    font = pygame.font.Font('Fonts/18918.ttf', 100)
    text = font.render("The Descent", True, (i, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    surf.blit(text, (text_x, text_y))


def pressenter(surf, screensize, i):
    width, height = screensize
    font = pygame.font.Font('Fonts/17238.otf', 20)
    text = font.render("Нажмите Enter чтобы продолжить...", True, (i, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 + 100
    surf.blit(text, (text_x, text_y))


def finalcaption(surf, screensize, i, t):
    width, height = screensize
    font = pygame.font.Font('Fonts/18918.ttf', 100)
    text = font.render(f"YOU WON IN {t}", True, (i, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    surf.blit(text, (text_x, text_y))

def TOP(surf, screensize, tt):
    width, height = screensize
    t = ''
    for i in tt:
        tt += i
    font = pygame.font.Font('Fonts/17238.otf', 20)
    text = font.render(f"TOP\n{t}", True, (139, 0, 0))
    text_x = width // 2 - text.get_width() // 2 + 350
    text_y = height // 2 - text.get_height() // 2 - 400
    surf.blit(text, (text_x, text_y))