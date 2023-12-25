import pygame
import random
import math

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


#keeping score
score=0

#Adding player
playerimg=pygame.image.load("player.png")
playerX=370
playerY=495
playerX_change=0

def player(x,y):
    screen.blit(playerimg,(x,y))

#Adding enemy
enemyimg=pygame.image.load("enemy.png")
enemyX=random.randint(0,735)
enemyY=random.randint(50,150)
enemyX_change=0.4
enemyY_change=40

def enemy(x,y):
    screen.blit(enemyimg,(x,y))

#Adding bullet
#Ready- Bullet cannot be seen on the screen
#Fire- Bullet is moving in screen    
bulletimg=pygame.image.load("bullet.png")
bulletX=0
bulletY=495
bulletY_change=0.6   
bullet_state="ready"

def fire_bullet(x,y):
    global bullet_state   #so that bullet_state can be changed inside the function
    bullet_state="fire"
    screen.blit(bulletimg,(x+16, y+10))

def is_collision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    return False

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
            if event.key==pygame.K_SPACE:
                #only shoot when bullet is not on screen
                if bullet_state=="ready":
                    # get current x coordinate of player
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
                
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
        enemyX_change=0.4
        enemyY+=enemyY_change
    elif enemyX>=736:
        enemyX_change=-0.4
        enemyY+=enemyY_change

    #bullet movement
    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    if bulletY<=0:
        bulletY=495
        bullet_state="ready"  

    #collision
    collision=is_collision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY=495
        bullet_state="ready"
        score+=1
        enemyX=random.randint(0,735)
        enemyY=random.randint(50,150)

    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()