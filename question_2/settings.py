import pygame
# constants for width and height of screen
screenWidth = 800
screenHeight = 600
FPS = 60
# color for screen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Side-Scrolling 2D Game with Human-Like Characters")
clock = pygame.time.Clock()
# images from local machine and you have to change the path according to your desire
playerImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\player.png').convert_alpha()
enemyImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\pngtree.png').convert_alpha()
bossImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\boss.png').convert_alpha()
projectileImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\s.png').convert_alpha()
collectibleImg = pygame.image.load(r'C:\Users\Speed\Pictures\final-group-assignment-python-code\question_2\sdd.png').convert_alpha()
# calling the functions
playerImg = pygame.transform.scale(playerImg, (50, 100))
enemyImg = pygame.transform.scale(enemyImg, (50, 50))
projectileImg = pygame.transform.scale(projectileImg, (10, 20))
collectibleImg = pygame.transform.scale(collectibleImg, (30, 30))

score = 0
lives = 3
level = 1
# same as abovee
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
