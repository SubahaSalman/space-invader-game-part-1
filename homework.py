# import math 
# import random
# import pygame


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 500
# PLAYER_START_X = 370
# PLAYER_START_Y = 380
# ENEMY_START_Y_MIN = 50
# ENEMY_START_Y_MAX = 150
# ENEMY_SPEED_X = 4
# ENEMY_SPEED_Y = 40
# BULLET_SPEED_Y = 10
# COLLISION_DISTANCE = 26

# pygame.init()

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background = pygame.image.load('background.png')
# enemies_hit = 0

# pygame.display.set_caption("Space Invader")
# icon = pygame.image.load('ufo.png')
# pygame.display.set_icon(icon)
# pygame.display.set_caption(enemies_hit)

# playerImg = pygame.image.load('player.png')
# playerX = PLAYER_START_X
# playerY = PLAYER_START_Y
# playerX_change = 0

# enemy1Img = []
# enemy1X = []
# enemy1Y = []
# enemy1X_change = []
# enemy1Y_change = []
# num_of_enemies1 = 6

# for _i in range(num_of_enemies1):
#     enemy1Img.append(pygame.image.load('enemy.png'))
#     enemy1X.append(random.randint(0, SCREEN_WIDTH - 64))
#     enemy1Y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
#     enemy1X_change.append(ENEMY_SPEED_X)
#     enemy1Y_change.append(ENEMY_SPEED_Y)

# enemy2Img = []
# enemy2X = []
# enemy2Y = []
# enemy2X_change = []
# enemy2Y_change = []
# num_of_enemies2 = 7

# for _i in range(num_of_enemies2):
#     enemy2Img.append(pygame.image.load('enemy2.png'))
#     enemy2X.append(random.randint(0, SCREEN_WIDTH - 64))
#     enemy2Y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
#     enemy2X_change.append(ENEMY_SPEED_X)
#     enemy2Y_change.append(ENEMY_SPEED_Y)

# COLLISION_DISTANCE


# if playerImg.COLLISION_DISTANCE(enemy2Img)== 0:
#     enemies_hit = enemies_hit+1 

import pygame
import random
import math

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

# Player settings
PLAYER_START_X = 370
PLAYER_START_Y = 380
PLAYER_SPEED = 5

# Enemy settings
NUM_ENEMIES = 7
ENEMY_SPEED = 3

# Collision
COLLISION_DISTANCE = 40

# Init pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision Game")

# Load images
playerImg = pygame.image.load('player.png')
enemyImg = pygame.image.load('enemy.png')
background = pygame.image.load('background.png')

# Player
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemies
enemyX = []
enemyY = []
enemyX_change = []

for i in range(NUM_ENEMIES):
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(ENEMY_SPEED)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Collision function
def is_collision(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance < COLLISION_DISTANCE

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                playerX_change = PLAYER_SPEED

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    playerX += playerX_change

    # Keep player inside screen
    if playerX < 0:
        playerX = 0
    elif playerX > SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64

    # Enemy movement + collision
    for i in range(NUM_ENEMIES):
        enemyX[i] += enemyX_change[i]

        # Bounce enemies left/right
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += 40

        # Collision check
        if is_collision(playerX, playerY, enemyX[i], enemyY[i]):
            score += 1

            # Reset enemy
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(50, 150)

        # Draw enemy
        screen.blit(enemyImg, (enemyX[i], enemyY[i]))

    # Draw player
    screen.blit(playerImg, (playerX, playerY))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()