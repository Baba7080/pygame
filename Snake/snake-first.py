import pygame, sys
from pygame.locals import *
import random
import os
pygame.init()
screen_width=900
screen_height=600
root = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("snake game")

WHITE = (255, 255, 255)
RED = (255,0,0)
black=(0,0,0)
snake_x = 45
snake_y = 60
vilocity_x= 0
vilocity_y= 0
food_x= random.randint(0,screen_width)
food_y=random.randint(0,screen_height)
score= 0
snake_size= 30
snake_size_for= 15
FPS = 30
fpsClock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def text_score(text,color,x,y):
    screen_text = font.render(text,True,color)
    root.blit(screen_text,[x,y])


while True:
   for event in pygame.event.get():
         if event.type == QUIT:

             sys.exit()


         if event.type ==pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                  vilocity_x = 5
                  vilocity_y = 0
             if event.key == pygame.K_LEFT:
                 vilocity_x = -5
                 vilocity_y = 0
             if event.key == pygame.K_UP:
                 vilocity_y = -5
                 vilocity_x = 0
             if event.key == pygame.K_DOWN:
                 vilocity_y = 5
                 vilocity_x = 0
             if event.key == pygame.K_SPACE:
                 os.system("pause")
             if event.key == pygame.K_s:
                 os.system("continue")



   snake_x = snake_x + vilocity_x
   snake_y = snake_y + vilocity_y
   if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
       score +=1
       food_x = random.randint(0, screen_width)
       food_y = random.randint(0, screen_height)

   root.fill(black)
   text_score("Score :" + str(score * 5), RED, 5, 5)
   pygame.draw.rect(root,WHITE,[food_x, food_y, snake_size, snake_size])
   pygame.draw.rect(root, RED, [snake_x, snake_y, 10, 10])

   pygame.display.update()
   fpsClock.tick(FPS)
pygame.quit()
quit()
