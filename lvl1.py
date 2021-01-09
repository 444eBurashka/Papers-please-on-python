import pygame
import ctypes
import os
import sys
import random
user = ctypes.windll.user32
pygame.init()
size = (user.GetSystemMetrics(0), user.GetSystemMetrics(1))
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("1.png", -1)
    image_back = load_image("2.png", -1)

    def __init__(self, *group):
        super().__init__(*group)
        size = (user.GetSystemMetrics(0), user.GetSystemMetrics(1))
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = size[1] - self.rect.height
        self.step = 1
        self.image_back = Bomb.image_back

    def update(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x -= self.step
                if self.rect.x < 0:
                    self.rect.x = 0
                self.image = self.image_back
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.step
                if self.rect.x > size[0] - self.rect.width:
                    self.rect.x = size[0] - self.rect.width
                self.image = Bomb.image


if __name__ == '__main__':
    pygame.display.set_caption('xxx')
    running = True
    all_sprites = pygame.sprite.Group()
    Bomb(all_sprites)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    running = False
        screen.fill((35, 35, 35))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()