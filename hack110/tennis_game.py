"""Tennis game! User moves the slider at the bottom of the screen to hit the ball as long as possible!"""

___author___ = "Prateek Mishra and Ishaan Balakrishnan"

import pygame
import math

# Initialize the pygame
pygame.init()

# create the screen
WIDTH = 500
HEIGHT = 700
BACKGROUND_COLOR = (255, 165, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Racket
racketImg = pygame.image.load('hack110/images/tennis-racket.png')
racketImg = pygame.transform.scale(racketImg, (64, 64))
racketX = WIDTH/2 - 32
racketY = 550
racketX_change = 0

# Ball
ballImg = pygame.image.load('hack110/images/tennisball.png')
ballImg = pygame.transform.scale(ballImg, (32, 32))
ballX = WIDTH/2 - 16
ballY = 200
ballX_change = 0
ballY_change = 0
ballX_speed = 600
ballY_speed = 300

# Clock
FramePerSec = pygame.time.Clock()

# Title and Icon
pygame.display.set_caption("Bouncy Tennis")
icon = pygame.image.load('hack110/images/tennis.png')
pygame.display.set_icon(icon)


def racket(x, y):
    screen.blit(racketImg, (x, y))

def ball(x, y):
    screen.blit(ballImg, (x, y))

def isCollision(ballX, ballY, racketX, racketY):
    distance = math.sqrt((math.pow(ballX-racketX, 2)) + (math.pow(ballY-racketY, 2)))
    if distance < 30:
        return True
    else:
        return False

# Game loop
running = True
while running:

    screen.fill(BACKGROUND_COLOR)
    milli = FramePerSec.tick()
    seconds = milli/1000.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is pressed, check if its left or right
        if event.type == pygame.KEYDOWN: # pressing any key 
            if event.key == pygame.K_LEFT:
                racketX_change -= 0.2
            if event.key == pygame.K_RIGHT:
                racketX_change += 0.2
        
        if event.type == pygame.KEYUP: # releasing the press of a key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                racketX_change = 0

    racketX += racketX_change
    if racketX <= 0:
        racketX = 0
    if racketX > WIDTH - 64:
        racketX = WIDTH - 64

    ballX_change = seconds * ballX_speed
    ballY_change = seconds * ballY_speed
    ballX += ballX_change
    ballY += ballY_change
    if ballX < 0:
        ballX_speed *= -1
    if ballX > WIDTH-32:
        ballX_speed *= -1
    if ballY > HEIGHT-32:
        ballY_speed *= -1
    if ballY < 0:
        ballY_speed *= -1


    # Collision
    collision: bool = isCollision(ballX, ballY, racketX, racketY)
    if collision:
        ballX_speed *= -1
        ballY_speed *= -1


    racket(racketX, racketY)
    ball(ballX, ballY)

    pygame.display.update()