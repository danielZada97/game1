import pygame
import numpy as np
import math

#initialize pygame
pygame.init()
#screen resolution ,icon and name and background
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
bulletY_default=SCREEN_HEIGHT-120
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space invaders")
icon=pygame.image.load("logo.png")
pygame.display.set_icon(icon)
background=pygame.image.load("background.jpg")

#player
playerImage=pygame.image.load("player.png")
playerX=SCREEN_WIDTH/2-50
playerY=SCREEN_HEIGHT-75
playerX_speed=0.3
def player(x,y):
    screen.blit(playerImage,(x,y))
#enemy
enemyImage=[]
enemyX=[]
enemyY=[]
enemy_speed=2
enemyX_change=[]
enemyY_change=[]
number_of_enemies=6

for i in range(number_of_enemies):
    enemyImage.append(pygame.image.load("enemati.png"))
    enemyX.append(0)
    enemyY.append(0)
    enemyX_change.append(0.5)
    enemyY_change.append(40)
#make enemy image
def enemy(x,y,i):
    screen.blit(enemyImage[i],(x,y))

#bullet
#ready state means the bullet is ready to being used
#fire=statee of being fired
bulletImage=pygame.image.load("laser_bullet.png")
bulletX=0
bulletY=bulletY_default
bullet_speed=0.5
bullet_state="ready"

#summon bullet
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImage,(x+8,y+5))
#check for a collision, if the distance between 2 point is less then 27 pixels
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=(math.sqrt(math.pow((enemyX-bulletX),2)+math.pow((enemyY-bulletY),2)))
    return True if distance <= 27 else False
run=True
while run:
    screen.fill((0,0,0))
    #set background
    screen.blit(background,(0,0))
  
    player(playerX,playerY)
    
    

   #check for bullet state change
    if bullet_state is "fire":
         fire_bullet(bulletX,bulletY)
         bulletY-=bullet_speed
         if bulletY<=0:
              bullet_state="ready"
              bulletY=bulletY_default
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]==True:
        playerX-=playerX_speed
        if playerX<=0:
            playerX=0
    elif key[pygame.K_RIGHT]==True:
         playerX+=playerX_speed
   #fire bullet
    elif key[pygame.K_SPACE]==True:
         bulletX=playerX
         fire_bullet(bulletX,playerY)
         
    #check for user boundry so it wont go out of the screen
    if playerX<=0:
            playerX=0
    if playerX>=(SCREEN_WIDTH-64):
            playerX=736
    #check for enemy place so it wont go out of the screen
    #move enemy: goes right, hit boundry, go down then go left etc...
    for i in range(number_of_enemies):
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
                enemyX_change[i]=0.5
                enemyY[i]+=enemyY_change[i]
                

        elif enemyX[i]>=(SCREEN_WIDTH-64):
            enemyX_change[i]=-0.5
            enemyY[i]+=enemyY_change[i]
        #handle collision of bullet and enemy
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
             bulletY=bulletY_default
             bullet_state="ready"
        enemy(enemyX[i],enemyY[i],i)
        
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                run=False
    pygame.display.update()
pygame.quit()