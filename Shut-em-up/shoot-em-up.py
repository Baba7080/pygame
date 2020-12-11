import pygame
import sys
from pygame import *
import random
import os

#colorr
gray =  (100,100,100)
navyblue = (60,60,100)
white = (255,255,255)
red = (255,255,255)
black =(0,0,0)
blue =(0,0,255)
yellow = (255,255,0)
#screen_design.......
width = 550
height = 600
screen_height =(height-10)

#object
food_x= 45
food_y= 45
#player
vilocity_x = 0
vilocity_y = 0
roc_x = 45
roc_y = height-150
rect_x= 45
rect_y= height/2
#bullet
bul_y= 650
bul_x = 0
bullet_speed = 10
bullet_state = "ready"
pos_rec_X_1 = width-150
pos_rec_X_2 =width-200
pos_rec_y_1= 300
pos_rec_y_2= height-450
#object2
size_obj =  45
coordinate_obj_x = width - 50
coordinate_obj_y = 50
cx1 = 30
cy1 = 30
cx2 = width/2
cy2 = 30
meteor_x=  width-300
meteor_y = 650
meteorx2 = width
meteory2 = 55
mx1= width
my1 = 40
mx2 = width
my2 = 40
lx2 = width
ly2 = 75

speed_x = 350
speed_y = 75

speed_xx = 400
speed_yy = 60





#score
score = 0

FPS = 90
fpsClock = pygame.time.Clock()
#image_loader
background = pygame.image.load("bbbb\myimage.jpg")
meteor = pygame.image.load("bbbb\meteorSmall.png")
meteor2 = pygame.image.load("bbbb\meteorBig.png")
rocket = pygame.image.load("bbbb\playerRight.png")
bbullet = pygame.image.load("bbbb\gunn.png")
speed1 = pygame.image.load("bbbb\speedline.png")
leser = pygame.image.load("bbbb\laserRedShot.png")
leser2 = pygame.image.load("bbbb\laserGreenShot.png")
l2 =leser2.get_rect()
r = rocket.get_rect()
b =background.get_rect()
s = speed1.get_rect()
b = bbullet.get_rect()
l= leser.get_rect()


pygame.init()
pygame.mixer.init()
root = pygame.display.set_mode((width,height))
pygame.display.set_caption("shoot'em up")

pygame.mixer.music.load("bbbb\muss.ogg")
#pygame.mixer.music.load("bbbb\Jannat.mp3")
#pygame.mixer.music.play(0)

font = pygame.font.SysFont(None, 55)
def text_score(text,color,x,y):
    screen_text = font.render(text,True,color)
    root.blit(screen_text,[x,y])



def bull_ready(x,y):
    global bullet_state
    bullet_state = "fire"
    root.blit(bbullet,(x, y-250))







while True:


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vilocity_x = 5
                vilocity_y = 0
            if event.key == pygame.K_LEFT:
                vilocity_x = -5
                vilocity_y = 0
            if event.key == pygame.K_SPACE:
               bul_x=roc_x
               bull_ready(bul_x,bul_y)
               bullet_speed =-10






        if roc_x >= width:
            vilocity_x =-5
            vilocity_y = 0




    roc_x = roc_x  + vilocity_x
    roc_y = vilocity_y +roc_y
    coordinate_obj_y = 65
    coordinate_obj_x = coordinate_obj_x - 3
   #bullet fire


    if roc_x >= (width -90):
         vilocity_x = 0
         roc_x = roc_x +vilocity_x
    if roc_x <= -10:
        vilocity_x = 0
        roc_x = roc_x +vilocity_x



    if abs(bul_x - coordinate_obj_x) < 40 and abs(bul_y - coordinate_obj_y) < 40:
        score +=1
        pygame.mixer.music.play()
        coordinate_obj_x = width
        coordinate_obj_y = 70

    if abs(bul_x- meteorx2) < 70 and abs(bul_y - meteory2) < 70:
        score +=1
        pygame.mixer.music.play()
        meteorx2 = width
        meteory2 = 100
    if abs(bul_x - meteor_x) < 40 and abs(bul_y - meteor_y) < 40:
        score +=1
        pygame.mixer.music.play()
        meteor_x= height/3
        meteor_y =0
    if abs(bul_x - mx1) < 40 and abs(bul_y - my1) < 40:
        score +=1
        pygame.mixer.music.play()
        mx1 = width/2
        my1 = 40
    if abs(bul_x - lx2) < 40 and abs(bul_y - lx2) < 40:
        score += 1
        pygame.mixer.music.play()
        lx2 = width / 2
        lx2 = 40
    if abs(bul_x - pos_rec_X_1) < 40 and abs(bul_y - pos_rec_y_1) < 40:
        score += 1
        pygame.mixer.music.play()
        pos_rec_X_1 = width / 2
        pos_rec_y_1 = 40
    if coordinate_obj_x<=0:
        coordinate_obj_x = width
        coordinate_obj_y= 65
    if speed_x <= 0:
        speed_x = width
        speed_y =75
    if speed_xx<=0:
        speed_xx = width-100
        speed_yy=  90
    if mx1 <= 0:
       mx1 =width
       my1 = 40
    if meteor_x <= 0:
        meteor_x= width
        meteor_y = 100
    if lx2 <= 0:
        ly2 = 65
        lx2 =width
    if meteorx2<=0:
        meteorx2= width +200
        meteory2 = 55
    if pos_rec_X_2 <=0:
        pos_rec_X_2 = width
        pos_rec_y_2 = 150
    if pos_rec_X_1 <= 0:
        pos_rec_X_1 = width + 139
        pos_rec_y_1 = 300
    meteor_x = meteor_x -1
    meteor_y = 100
    speed_x = speed_x -3
    speed_y = speed_y +10

    speed_xx = speed_xx -1
    speed_yy = speed_yy + 15
    mx1 = mx1 -3
    my1 = 55
    mx2 = mx2 -3
    my2 = 100
    lx2 = lx2 -4
    ly2 = 50
    meteorx2 -=2
    meteory2 =0
    pos_rec_X_1 -=2
    pos_rec_y_1= 155
    pos_rec_X_2 -=3
    pos_rec_y_2 = 175

    #pygame.mixer.music.stop()

    root.fill(black)
    root.blit(background, [0, 0])
    text_score("Score :" + str(score),red, 5, 5)

    pygame.draw.rect(root, gray,[coordinate_obj_x,coordinate_obj_y,size_obj,size_obj])
    root.blit(meteor, (meteor_x,meteor_y))
    root.blit(meteor2,(meteorx2,meteory2))
    root.blit(meteor,(meteor_x+150, meteor_y+50))
    root.blit(leser, (mx1, my1))
    root.blit(leser, (mx2, my2))
    root.blit(leser2,(lx2,ly2))
    root.blit(speed1, (speed_x, speed_y))
    root.blit(speed1, (speed_xx, speed_yy))
    pygame.draw.rect(root, yellow, [pos_rec_X_1,pos_rec_y_1, size_obj, size_obj])
    pygame.draw.rect(root, gray, [pos_rec_X_2,pos_rec_y_2, size_obj, size_obj])
    root.blit(rocket, (roc_x, roc_y))




    #scores

    #text_score("Score :" + str(score * 5), red, 5, 5)

    if bullet_state == "fire":
        bull_ready(bul_x, bul_y)
        bul_y = bul_y + bullet_speed
    if bul_y <=0:
        bullet_state="ready"
        bul_y=650
    pygame.display.update()

    fpsClock.tick(FPS)
sys.exit()