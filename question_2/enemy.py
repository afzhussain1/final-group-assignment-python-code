import pygame
import random
from settings import screenWidth, enemyImg

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemyImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > screenWidth or self.rect.left < 0:
            self.speed_x = -self.speed_x
