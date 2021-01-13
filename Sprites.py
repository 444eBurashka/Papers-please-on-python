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

    def __init__(self, screensize, *group):
        super().__init__(*group)
        self.size = screensize
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
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
        

if __name__ == '__main__':
    pygame.display.set_caption('xxx')
    running = True
    sprites = pygame.sprite.Group()
    hero = Player()
    sprites.add(hero)
    left = False
    right = False
    up = False
    while running:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DELETE:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
        screen.fill((35, 35, 35))
        sprites.draw(screen)
        hero.update(left, right, up)
        pygame.display.flip()
