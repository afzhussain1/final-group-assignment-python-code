

import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Display game
screenWidth = 800  # Fixed width for testing
screenHeight = 600  # Fixed height for testing
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to adjust the screen size
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Side-Scrolling 2D Game with Human-Like Characters")
clock = pygame.time.Clock()

# Load images (update these paths)
playerImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\player.png').convert_alpha()
enemyImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\pngtree.png').convert_alpha()
bossImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\boss.png').convert_alpha()
projectileImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\s.png').convert_alpha()
collectibleImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\sdd.png').convert_alpha()

# Check if the images exist
for img in [playerImg, enemyImg, bossImg, projectileImg, collectibleImg]:
    if img is None:
        print("Image not found:", img)

# Resize images
playerImg = pygame.transform.scale(playerImg, (50, 100))  
enemyImg = pygame.transform.scale(enemyImg, (50, 50))      
projectileImg = pygame.transform.scale(projectileImg, (10, 20))  
collectibleImg = pygame.transform.scale(collectibleImg, (30, 30))  

# Constants
score = 0
lives = 3
level = 1

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = playerImg
        self.rect = self.image.get_rect()
        self.rect.x = screenWidth // 2  # player size screen
        self.rect.y = screenHeight - 200  #  height for charactor
        self.speed_x = 5
        self.speed_y = 0
        self.gravity = 0.5
        self.jump_power = 10
        self.jumping = False
        self.shooting_cooldown = 500
        self.last_shot = pygame.time.get_ticks()

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
        if self.rect.y >= screenHeight - 200:  # Adjusted height
            self.rect.y = screenHeight - 200
            self.jumping = False

        # Boundary checks
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screenWidth - self.rect.width:
            self.rect.x = screenWidth - self.rect.width

        # Handle shooting
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

#  Groups
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
collectibles = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    print(f"Player Position: {player.rect.x}, {player.rect.y}")
    
    # Collisions
    if pygame.sprite.spritecollide(player, enemies, True):
        lives -= 1

    if pygame.sprite.spritecollide(player, collectibles, True):
        score += 10

    enemy_hits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
    for hit in enemy_hits:
        score += 5
        enemy = Enemy(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200))
        all_sprites.add(enemy)
        enemies.add(enemy)

    if lives <= 0:
        print("Game Over! Final Score:", score)
        running = False  

    if len(enemies) == 0:
        level += 1
        for i in range(level * 5):  
            enemy = Enemy(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200))
            all_sprites.add(enemy)
            enemies.add(enemy)

    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Show score, lives, and level
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    lives_text = font.render(f'Lives: {lives}', True, BLACK)
    level_text = font.render(f'Level: {level}', True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (screenWidth - 100, 10))
    screen.blit(level_text, (screenWidth // 2 - 50, 10))

    # Refresh screen
    pygame.display.flip()
    
    clock.tick(FPS)
# exit to the game
pygame.quit()



