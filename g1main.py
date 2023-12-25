import pygame
import random

#initialize pygame
pygame.init() 

#create screen
screen = pygame.display.set_mode((800,600))

#Create background
background=pygame.image.load("space_bg.jpeg")

#title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#Adding player
playerimg=pygame.image.load("player.png")
playerX=370
playerY=495
playerX_change=0

def player(x,y):
    screen.blit(playerimg,(x,y))

#Adding player
enemyimg=pygame.image.load("enemy.png")
enemyX=random.randint(0,800)
enemyY=random.randint(50,150)
enemyX_change=0.3
enemyY_change=40

def enemy(x,y):
    screen.blit(enemyimg,(x,y))

#Game Loop
running = True
while running:
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False  
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.3
            if event.key==pygame.K_RIGHT:
                playerX_change=0.3
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

    #checking boundaries of spaceship so it doesn't get out of bounds
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736    
    
    #enemy movements
    enemyX+=enemyX_change
    if enemyX<=0:
        enemyX_change=0.3
        enemyY+=enemyY_change
    elif enemyX>=736:
        enemyX_change=-0.3
        enemyY+=enemyY_change
        
    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()