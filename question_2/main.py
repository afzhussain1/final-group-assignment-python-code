
import pygame
import random
from settings import *
from player import Player
from enemy import Enemy
from collectible import Collectible
#initiate the game
pygame.init()
# to call the class
player = Player()
all_sprites.add(player)
# Apply logic 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
# collition between the enemy and pplayer
    if pygame.sprite.spritecollide(player, enemies, True):
        lives -= 1
# Same Logic as above
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
     # adjust the  screen size
    screen.fill(WHITE)
    all_sprites.draw(screen)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    lives_text = font.render(f'Lives: {lives}', True, BLACK)
    level_text = font.render(f'Level: {level}', True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (screenWidth - 100, 10))
    screen.blit(level_text, (screenWidth // 2 - 50, 10))

    pygame.display.flip()

    clock.tick(FPS)
# exit the game 
pygame.quit()
