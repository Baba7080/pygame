import pygame, sys
from pygame.locals import *
import pygame.mixer

width = 500
height = 450
black = (255,255,255)
vilox= 0
viloy = 0
carx = (width/2)-20
cary = height-100
car22x = (width/2)-20
car22y=-300
car33x= 150
car33y= -450
bannelx = 50
bannelx2= width - 100
bannely=height+100
bannely2= height
treex= -5
treey=200
rockx=-30
rocky=24
crossingy =10
viloxx=0
voliy=0
bariery = -300
FPS=100
y=15
car2x=width/3
car2y = 0
fpsclock= pygame.time.Clock()

root = pygame.display.set_mode((width,height))
pygame.display.set_caption("racing game")

bg = pygame.image.load("Back.png")
bannel = pygame.image.load("LeftBump.png")
road1= pygame.image.load("Road.png")
car  = pygame.image.load("CarBlue.png")
carRED  = pygame.image.load("CarRed.png")
carRED2  = pygame.image.load("CarRed.png")
carRED3  = pygame.image.load("CarRed.png")
tree = pygame.image.load("tree.png")
bannel2 = pygame.image.load("RightBump.png")
road= pygame.image.load("roadcar.png")
crossing = pygame.image.load("crossing.png")
house = pygame.image.load("sprite_tree.png")
ramp = pygame.image.load("sprite_ramp.png")
objcar = pygame.image.load("barrier.png")
mssg = pygame.image.load("pipe.png")
sprite_tree = pygame.image.load("sprite_tree_dead.png")

pygame.init()
pygame.mixer.init()

def massage():
    root.blit(mssg,(width/2,height/2))
while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                viloy= -6
                voliy= -6
            if event.key == pygame.K_LEFT:
                viloxx=-20
            if event.key == pygame.K_RIGHT:
                viloxx = 20
            if event.key == pygame.K_DOWN:
                viloy=2
                voliy=2
    if crossingy >= height:
        crossingy = -200

    if treey>=height:
        treey=-500
    if rocky>=height:
        rocky = -400
    if y ==height:
        y= -200
    if bariery == height:
        bariery = -400
    treey -=viloy
    rocky -=viloy
    crossingy-=voliy
    car2y -=viloy
    bariery -=viloy
    carx +=viloxx
    car22y -=viloy
    car33y -=-viloy



    if abs(carx - car33x)<130 and abs(cary-car33y)<100:
         print("sound")
         massage()
         pygame.mixer.music.load("pygame\\swoosh.wav")
         pygame.mixer.music.play()
         viloxx = 5

    if abs(carx - car22x)<100 and abs(cary-car22y)<100:
         print("sound")
         pygame.mixer.music.load("swoosh.wav")
         pygame.mixer.music.play()
         viloxx = 4
         massage()

    if abs(carx - car2x)<100 and abs(cary-car2y)<100:
         print("sound")
         pygame.mixer.music.load("swoosh.wav")
         pygame.mixer.music.play()
         viloxx = 5
    if abs(carx - bannelx2)<100 and abs(cary - bannely2)<500:
        viloxx = 0
    if abs(carx - bannelx) < 50 and abs(cary - bannely) <300:
        viloxx = 0
    if car2y >= height:
        car2y= -200
        massage()
    if car22y >= height:
        car22y = -200
        massage()




    root.fill(black)
    root.blit(bg ,(0,0))

    y -=viloy
    #for next window

    root.blit(road1, (120, 0))
    root.blit(crossing, (50, crossingy))
                                                #treex,treey, rockx,rocky
    root.blit(bannel,(50,0))
    root.blit(bannel, (width-100, 0))
    #root.blit(bg,(carx,cary+height))
    root.blit(bannel, (50, height))
    root.blit(house,(rockx,rocky))
    root.blit(tree,(treex,treey))
    root.blit(tree,(width-70,treey))
    root.blit(bannel2, (bannelx,bannely ))
    root.blit(bannel2, ( bannelx2,bannely2))
    root.blit(ramp,(150,100))
    root.blit(sprite_tree,(width,15))
    root.blit(carRED,(car2x-20,car2y+20))
    root.blit(objcar,(10,bariery))
    root.blit(carRED2, (car22x, car22y))
    root.blit(carRED3, (car33x , car33y))

    root.blit(car,(carx, cary))

    root.blit(sprite_tree, (400,  y))


    pygame.display.update()
    fpsclock.tick(FPS)

sys.exit()