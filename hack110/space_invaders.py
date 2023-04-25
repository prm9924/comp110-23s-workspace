"""Pygame tutorial!"""

import pygame
import random
import math

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("hack110/images/space_background.jpg")
background = pygame.transform.scale(background, (800, 700))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('hack110/images/spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('hack110/images/player_ship.png')
playerImg = pygame.transform.scale(playerImg, (60, 60))
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('hack110/images/alien.png')
enemyImg = pygame.transform.scale(enemyImg, (60, 60))
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0.25
enemyY_change = 40

# Bullet
# Ready - you can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('hack110/images/bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (32, 32))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = .4
bullet_state = "ready"

score = 0
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 30:
        return True
    else:
        return False

# Game loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is pressed, check if its left or right
        if event.type == pygame.KEYDOWN: # pressing any key 
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.3
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX  # get the current x coordinate of the spaceship
                    fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP: # releasing the press of a key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    if playerX >= 740:
        playerX = 740

    enemyX += enemyX_change
    
    if enemyX <= 0:
        enemyX_change = 0.25
        enemyY += enemyY_change
    if enemyX >= 740:
        enemyX_change = -0.25
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision: bool = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()