import pygame
from settings import collectibleImg

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = collectibleImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
