# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# #  display  game
# info = pygame.display.Info()
# # adjust the width and height of screen
# screenWidth = info.current_w
# screenHeight = info.current_h
# FPS = 60

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # function to adjust the screen size
# screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
# pygame.display.set_caption("Side-Scrolling 2D Game")
# clock = pygame.time.Clock()

# # Load images
# playerImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\player.png').convert_alpha()
# enemyImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\enemy.png').convert_alpha()
# projectileImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\miscellaneous-angle.png').convert_alpha()
# collectibleImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\sdd.png').convert_alpha()

# # constants
# score = 0
# lives = 3
# level = 1

# # Player Class to handle the player movement
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = playerImg
#         self.rect = self.image.get_rect()
#         self.rect.x = 50
#         self.rect.y = screenHeight - 100
#         self.speed_x = 5
#         self.speed_y = 0
#         self.gravity = 0.5
#         self.jump_power = 10
#         self.jumping = False
#         self.shooting_cooldown = 500
#         self.last_shot = pygame.time.get_ticks()

#     def update(self):
#         # Get key presses
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.rect.x -= self.speed_x
#         if keys[pygame.K_RIGHT]:
#             self.rect.x += self.speed_x
#         if keys[pygame.K_SPACE] and not self.jumping:
#             self.jumping = True
#             self.speed_y = -self.jump_power

#         # Apply gravity
#         self.speed_y += self.gravity
#         self.rect.y += self.speed_y
#         if self.rect.y >= screenHeight - 100:
#             self.rect.y = screenHeight - 100
#             self.jumping = False

#         # handle the  Shooting
#         if keys[pygame.K_f]:
#             now = pygame.time.get_ticks()
#             if now - self.last_shot >= self.shooting_cooldown:
#                 self.last_shot = now
#                 self.shoot()

#     def shoot(self):
#         projectile = Projectile(self.rect.centerx, self.rect.top)
#         all_sprites.add(projectile)
#         projectiles.add(projectile)

# # Projectile Class
# class Projectile(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = projectileImg
#         self.rect = self.image.get_rect()
#         self.rect.centerx = x
#         self.rect.top = y
#         self.speed_y = -10

#     def update(self):
#         self.rect.y += self.speed_y
#         if self.rect.bottom < 0:
#             self.kill()

# # Enemy Class
# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = enemyImg
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])

#     def update(self):
#         self.rect.x += self.speed_x
#         if self.rect.right > screenWidth or self.rect.left < 0:
#             self.speed_x = -self.speed_x

# # Collectible Class
# class Collectible(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = collectibleImg
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y

# all_sprites = pygame.sprite.Group()
# projectiles = pygame.sprite.Group()
# enemies = pygame.sprite.Group()
# collectibles = pygame.sprite.Group()

# player = Player()
# all_sprites.add(player)

# # logic to handle
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Update all sprites
#     all_sprites.update()

#     #  collisions between player and enemies
#     if pygame.sprite.spritecollide(player, enemies, True):
#         lives -= 1

#     #  collisions between player and collectibles
#     if pygame.sprite.spritecollide(player, collectibles, True):
#         score += 10

#     #  projectile collisions with enemies
#     enemy_hits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
#     for hit in enemy_hits:
#         score += 5
#         enemy = Enemy(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200))
#         all_sprites.add(enemy)
#         enemies.add(enemy)
#       # if condition to check
#     if lives <= 0:
#         running = False  

#     if len(enemies) == 0:
#         level += 1
#         for i in range(level * 5):  
#             enemy = Enemy(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200))
#             all_sprites.add(enemy)
#             enemies.add(enemy)

#     screen.fill(WHITE)
#     all_sprites.draw(screen)

#     #   show the score, lives, and level
#     font = pygame.font.Font(None, 36)
#     score_text = font.render(f'Score: {score}', True, BLACK)
#     lives_text = font.render(f'Lives: {lives}', True, BLACK)
#     level_text = font.render(f'Level: {level}', True, BLACK)
#     screen.blit(score_text, (10, 10))
#     screen.blit(lives_text, (screenWidth - 100, 10))
#     screen.blit(level_text, (screenWidth // 2 - 50, 10))

#     # call the function
#     pygame.display.flip()
#     clock.tick(FPS)

# pygame.quit()


# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Display game
# info = pygame.display.Info()
# screenWidth = info.current_w
# screenHeight = info.current_h
# FPS = 60

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Screen setup
# screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
# pygame.display.set_caption("Side-Scrolling 2D Game")
# clock = pygame.time.Clock()

# # Load images
# playerImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\player.png').convert_alpha()
# enemyImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\enemy.png').convert_alpha()
# bossImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\boss.png').convert_alpha()
# projectileImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\miscellaneous-angle.png').convert_alpha()
# collectibleImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\sdd.png').convert_alpha()

# # Constants
# score = 0
# lives = 3
# level = 1

# # Player Class
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = playerImg
#         self.rect = self.image.get_rect()
#         self.rect.center = (screenWidth // 2, screenHeight // 2)  # Center the player
#         self.speed_x = 5
#         self.speed_y = 0
#         self.gravity = 0.5
#         self.jump_power = 10
#         self.jumping = False
#         self.health = 100

#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.rect.x -= self.speed_x
#         if keys[pygame.K_RIGHT]:
#             self.rect.x += self.speed_x
#         if keys[pygame.K_SPACE] and not self.jumping:
#             self.jumping = True
#             self.speed_y = -self.jump_power

#         # Apply gravity
#         self.speed_y += self.gravity
#         self.rect.y += self.speed_y

#         # Prevent falling below the ground
#         if self.rect.y >= screenHeight // 2:
#             self.rect.y = screenHeight // 2
#             self.jumping = False
#             self.speed_y = 0

#         # Keep the player within screen bounds
#         if self.rect.x < 0:
#             self.rect.x = 0
#         if self.rect.x > screenWidth - self.rect.width:
#             self.rect.x = screenWidth - self.rect.width

#     def shoot(self):
#         projectile = Projectile(self.rect.centerx, self.rect.top)
#         all_sprites.add(projectile)
#         projectiles.add(projectile)

#     def draw_health_bar(self, screen):
#         pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y - 10, self.rect.width, 5))
#         pygame.draw.rect(screen, GREEN, (self.rect.x, self.rect.y - 10, self.rect.width * (self.health / 100), 5))

# # Projectile Class
# class Projectile(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = projectileImg
#         self.rect = self.image.get_rect()
#         self.rect.centerx = x
#         self.rect.top = y
#         self.speed_y = -10

#     def update(self):
#         self.rect.y += self.speed_y
#         if self.rect.bottom < 0:
#             self.kill()

# # Enemy Class
# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = enemyImg
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])
#         self.health = 30

#     def update(self):
#         self.rect.x += self.speed_x
#         if self.rect.right > screenWidth or self.rect.left < 0:
#             self.speed_x = -self.speed_x

#     def draw_health_bar(self, screen):
#         pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y - 10, self.rect.width, 5))
#         pygame.draw.rect(screen, GREEN, (self.rect.x, self.rect.y - 10, self.rect.width * (self.health / 30), 5))

# # Boss Class
# class Boss(Enemy):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.image = bossImg
#         self.health = 100

# # Collectible Class
# class Collectible(pygame.sprite.Sprite):
#     def __init__(self, x, y, type):
#         super().__init__()
#         self.image = collectibleImg
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.type = type

#     def apply_effect(self, player):
#         if self.type == 'health':
#             player.health = min(player.health + 20, 100)
#         elif self.type == 'life':
#             global lives
#             lives += 1

# class Camera:
#     def __init__(self, player):
#         self.x = 0
#         self.y = 0
#         self.player = player

#     def update(self):
#         self.x = self.player.rect.x - screenWidth // 2
#         self.y = self.player.rect.y - screenHeight // 2

# all_sprites = pygame.sprite.Group()
# projectiles = pygame.sprite.Group()
# enemies = pygame.sprite.Group()
# collectibles = pygame.sprite.Group()

# player = Player()
# all_sprites.add(player)
# camera = Camera(player)

# def spawn_collectible():
#     type = random.choice(['health', 'life'])
#     collectible = Collectible(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200), type)
#     all_sprites.add(collectible)
#     collectibles.add(collectible)

# # Game Over Screen
# def game_over_screen():
#     screen.fill(BLACK)
#     font = pygame.font.Font(None, 74)
#     game_over_text = font.render("GAME OVER", True, WHITE)
#     screen.blit(game_over_text, (screenWidth // 2 - 150, screenHeight // 2 - 50))

#     restart_text = font.render("Press R to Restart", True, WHITE)
#     screen.blit(restart_text, (screenWidth // 2 - 200, screenHeight // 2 + 50))
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_r:
#                     waiting = False
#                     main()

# def main():
#     global score, lives, level

#     score = 0
#     lives = 3
#     level = 1

#     # Initial enemies
#     for i in range(5):
#         enemy = Enemy(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200))
#         all_sprites.add(enemy)
#         enemies.add(enemy)

#     # Main game loop
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Update all sprites
#         all_sprites.update()

#         # Update camera
#         camera.update()

#         # Check collisions
#         if pygame.sprite.spritecollide(player, enemies, True):
#             player.health -= 10
#             if player.health <= 0:
#                 lives -= 1
#                 player.health = 100
#                 if lives <= 0:
#                     running = False

#         if pygame.sprite.spritecollide(player, collectibles, True):
#             for collectible in pygame.sprite.spritecollide(player, collectibles, True):
#                 collectible.apply_effect(player)

#         enemy_hits = pygame.sprite.groupcollide(enemies, projectiles, False, True)
#         for enemy in enemy_hits:
#             enemy.health -= 10
#             if enemy.health <= 0:
#                 score += 5
#                 enemy.kill()
#                 if len(enemies) == 0:
#                     level += 1
#                     for i in range(level * 5):
#                         if level % 3 == 0 and i == level * 5 - 1:
#                             enemy = Boss(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200))
#                         else:
#                             enemy = Enemy(random.randint(100, screenWidth - 100), random.randint(100, screenHeight - 200))
#                         all_sprites.add(enemy)
#                         enemies.add(enemy)

#         # Clear the screen
#         screen.fill(WHITE)

#         # Draw everything
#         for sprite in all_sprites:
#             screen.blit(sprite.image, (sprite.rect.x - camera.x, sprite.rect.y - camera.y))

#         # Draw health bars
#         player.draw_health_bar(screen)
#         for enemy in enemies:
#             enemy.draw_health_bar(screen)

#         # Show the score, lives, and level
#         font = pygame.font.Font(None, 36)
#         score_text = font.render(f'Score: {score}', True, BLACK)
#         lives_text = font.render(f'Lives: {lives}', True, BLACK)
#         level_text = font.render(f'Level: {level}', True, BLACK)
#         screen.blit(score_text, (10, 10))
#         screen.blit(lives_text, (screenWidth - 100, 10))
#         screen.blit(level_text, (screenWidth // 2 - 50, 10))

#         pygame.display.flip()
#         clock.tick(FPS)

#     game_over_screen()

# main()
# pygame.quit()



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
enemyImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\enemy.png').convert_alpha()
bossImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\boss.png').convert_alpha()
projectileImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\miscellaneous-angle.png').convert_alpha()
collectibleImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\sdd.png').convert_alpha()

# Check if the images exist
for img in [playerImg, enemyImg, bossImg, projectileImg, collectibleImg]:
    if img is None:
        print("Image not found:", img)

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
        self.rect.x = screenWidth // 2  # Start player in the middle of the screen
        self.rect.y = screenHeight - 150  # Adjusted height for visibility
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

        # Apply gravity
        self.speed_y += self.gravity
        self.rect.y += self.speed_y
        if self.rect.y >= screenHeight - 150:  # Adjusted height
            self.rect.y = screenHeight - 150
            self.jumping = False

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

# Sprite Groups
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

    # Update all sprites
    all_sprites.update()

    # Debugging output
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

    # Draw everything
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

pygame.quit()




