import pygame
from settings import projectileImg

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = projectileImg
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
