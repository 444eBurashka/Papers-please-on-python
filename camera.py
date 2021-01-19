import pygame


class Camera(object):
    def __init__(self, camera_func, size, scr_size):
        self.camera_func = camera_func
        self.width = size[0]
        self.height = size[1]
        self.scr_width = scr_size[0]
        self.scr_height = scr_size[1]
        self.state = pygame.Rect(0, 0, size[0], size[1])

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect, self.scr_width, self.scr_height)


def camera_configure(camera, target_rect, width, height):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+width / 2, -t+height / 2

    l = min(0, l)
    l = max(-(camera.width-width), l)
    t = max(-(camera.height-height), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)