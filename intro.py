import pygame
import time

def intro(surf, screensize):
    width, height = screensize
    introsound = pygame.mixer.Sound('Music/intro.mp3')
    introsound.play()
    font = pygame.font.Font('Fonts/16905.ttf', 50)
    text1 = font.render("STEEL Gaming present", True, (139, 0, 0))
    text_x = width // 2 - text1.get_width() // 2
    text_y = height // 2 - text1.get_height() // 2 + 200
    surf.blit(text1, (text_x, text_y))
    font = pygame.font.Font('Fonts/18918.ttf', 100)
    text = font.render("The Descent", True, (139, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    surf.blit(text, (text_x, text_y))
    introsound.stop()


def main():
    pass