import pygame
from projectile import Projectile
from settings import screenWidth, screenHeight, playerImg, all_sprites, projectiles
# player class whith logics
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # adjust the size and rotaion and screen size as well
        self.image = playerImg
        self.rect = self.image.get_rect()
        self.rect.x = screenWidth // 2
        self.rect.y = screenHeight - 200
        self.speed_x = 5
        self.speed_y = 0
        self.gravity = 0.5
        self.jump_power = 10
        self.jumping = False
        self.shooting_cooldown = 500
        self.last_shot = pygame.time.get_ticks()
        #movemet against the X and Y axis
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_x
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.speed_y = -self.jump_power

        self.speed_y += self.gravity
        self.rect.y += self.speed_y
        if self.rect.y >= screenHeight - 200:
            self.rect.y = screenHeight - 200
            self.jumping = False

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screenWidth - self.rect.width:
            self.rect.x = screenWidth - self.rect.width

        if keys[pygame.K_f]:
            now = pygame.time.get_ticks()
            if now - self.last_shot >= self.shooting_cooldown:
                self.last_shot = now
                self.shoot()

    def shoot(self):
        projectile = Projectile(self.rect.centerx, self.rect.top)
        all_sprites.add(projectile)
        projectiles.add(projectile)
