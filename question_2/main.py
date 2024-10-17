import pygame
import random

# Initialize Pygame
pygame.init()

#  display  game
info = pygame.display.Info()
# adjust the width and height of screen
screenWidth = info.current_w
screenHeight = info.current_h
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# function to adjust the screen size
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
pygame.display.set_caption("Side-Scrolling 2D Game")
clock = pygame.time.Clock()

# Load images
playerImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\player.png').convert_alpha()
enemyImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\enemy.png').convert_alpha()
projectileImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\miscellaneous-angle.png').convert_alpha()
collectibleImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\sdd.png').convert_alpha()

# constants
score = 0
lives = 3
level = 1

# Player Class to handle the player movement
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = playerImg
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = screenHeight - 100
        self.speed_x = 5
        self.speed_y = 0
        self.gravity = 0.5
        self.jump_power = 10
        self.jumping = False
        self.shooting_cooldown = 500
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        # Get key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_x
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True
            self.speed_y = -self.jump_power

        # Apply gravity
        self.speed_y += self.gravity
        self.rect.y += self.speed_y
        if self.rect.y >= screenHeight - 100:
            self.rect.y = screenHeight - 100
            self.jumping = False

        # handle the  Shooting
        if keys[pygame.K_f]:
            now = pygame.time.get_ticks()
            if now - self.last_shot >= self.shooting_cooldown:
                self.last_shot = now
                self.shoot()

    def shoot(self):
        projectile = Projectile(self.rect.centerx, self.rect.top)
        all_sprites.add(projectile)
        projectiles.add(projectile)

# Projectile Class
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

# Enemy Class
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

# Collectible Class
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = collectibleImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
collectibles = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# logic to handle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    #  collisions between player and enemies
    if pygame.sprite.spritecollide(player, enemies, True):
        lives -= 1

    #  collisions between player and collectibles
    if pygame.sprite.spritecollide(player, collectibles, True):
        score += 10

    #  projectile collisions with enemies
    enemy_hits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
    for hit in enemy_hits:
        score += 5
        enemy = Enemy(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200))
        all_sprites.add(enemy)
        enemies.add(enemy)
      # if condition to check
    if lives <= 0:
        running = False  

    if len(enemies) == 0:
        level += 1
        for i in range(level * 5):  
            enemy = Enemy(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200))
            all_sprites.add(enemy)
            enemies.add(enemy)

    screen.fill(WHITE)
    all_sprites.draw(screen)

    #   show the score, lives, and level
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    lives_text = font.render(f'Lives: {lives}', True, BLACK)
    level_text = font.render(f'Level: {level}', True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (screenWidth - 100, 10))
    screen.blit(level_text, (screenWidth // 2 - 50, 10))

    # call the function
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
