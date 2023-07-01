import pygame
import numpy as np

#initialize pygame
pygame.init()
#screen resolution ,icon and name and background
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space invaders")
icon=pygame.image.load("logo.png")
pygame.display.set_icon(icon)
background=pygame.image.load("background.jpg")

#player
playerImage=pygame.image.load("player.png")
playerX=SCREEN_WIDTH/2-50
playerY=SCREEN_HEIGHT-75
player_speed=0.3
def player(x,y):
    screen.blit(playerImage,(x,y))
#enemy
enemyImage=pygame.image.load("enemy.png")
enemyY=0
enemyX=0
enemy_speed=0.3
enemyX_change=0
enemyY_change=0
def enemy(x,y):
    screen.blit(enemyImage,(x,y))




run=True
while run:
    screen.fill((0,0,0))
    #set background
    screen.blit(background,(0,0))
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    enemyX+=enemy_speed

   
    
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]==True:
        playerX-=player_speed
        if playerX<=0:
            playerX=0
    elif key[pygame.K_RIGHT]==True:
         playerX+=player_speed
         
    #check for user boundry so it wont go out of the screen
    if playerX<=0:
            playerX=0
    if playerX>=(SCREEN_WIDTH-64):
            playerX=736
    #check for enemy place so it wont go out of the screen
    if enemyX<=0:
            enemyX=0
            enemyY+=50
            enemy_speed=np.abs(enemy_speed)

    if enemyX>=(SCREEN_WIDTH-64):
            enemyX=736
            enemyY+=50
            enemy_speed=(enemy_speed-2*enemy_speed)
    #move enemy: goes right, hit boundry, go down then go left etc...
    
    
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                run=False
    pygame.display.update()
pygame.quit()