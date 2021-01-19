import pygame
import CONFIG
import os
import sys


GRAVITY = 0.2


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    image = load_image("1.png", -1)
    image_back = load_image("2.png", -1)

    def __init__(self, game_size, *group):
        super().__init__(*group)
        self.size = game_size
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = self.size[1] - self.rect.height
        self.step = 3
        self.onGround = True
        self.speedY = 0

    def update(self, left, right, up):
        if left:
            self.rect.x -= self.step
            if self.rect.x < 0:
                self.rect.x = 0
            self.image = Player.image_back
        if right:
            self.rect.x += self.step
            if self.rect.x > self.size[0] - self.rect.width:
                self.rect.x = self.size[0] - self.rect.width
            self.image = Player.image
        if up:
            if self.onGround:
                self.speedY = -10
                self.onGround = False
        if not self.onGround:
            self.speedY += GRAVITY
            self.rect.y += self.speedY
            if self.rect.y + self.rect.height > self.size[1]:
                self.rect.y = self.size[1] - self.rect.height
                self.onGround = True
        
        

class Smth(pygame.sprite.Sprite):
    image = load_image("3.png")

    def __init__(self, screensize, x, *group):
        super().__init__(*group)
        self.image = Smth.image
        self.g = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.size = screensize
        self.rect.y = self.size[1] - self.rect.height - 700
    
    def change(self):
        if self.g:
            self.image = load_image("3.png")
            self.g = False
        else:
            self.image = load_image("4.png")
            self.g = True


class PO(pygame.sprite.Sprite):
    image = load_image("po.png")

    def __init__(self, screensize, *group):
        super().__init__(*group)
        self.image = PO.image
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.size = screensize
        self.rect.y = self.size[1] - self.rect.height - 300


class Puzzle1(pygame.sprite.Sprite):
    image = load_image("puzzle1.png")

    def __init__(self, screensize, *group):
        super().__init__(*group)
        self.image = Puzzle1.image
        self.rect = self.image.get_rect()
        self.rect.x = 2500
        self.size = screensize
        self.rect.y = self.size[1] - self.rect.height - 400


class bricks(pygame.sprite.Sprite):
    image = load_image("Bricks.png")

    def __init__(self, screensize, x, y, *group):
        super().__init__(*group)
        self.image = bricks.image
        self.g = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.size = screensize
        self.rect.y = self.size[1] - self.rect.height - y


class gg1(pygame.sprite.Sprite):
    image = load_image("gg.png")

    def __init__(self, screensize, *group):
        super().__init__(*group)
        self.image = gg1.image
        self.g = False
        self.rect = self.image.get_rect()
        self.rect.x = 1500
        self.size = screensize
        self.rect.y = self.size[1] - self.rect.height - 600
    

    def change(self):
        if self.g:
            self.image = load_image("gg.png")
            self.g = False
        else:
            self.image = load_image("alfavit.png")
            self.g = True