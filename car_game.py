import pygame
from pygame.locals import *

size = width, height = (400, 800)
road_width = int(width/1.5)
roadmark = int(width/80)

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MEK's car game")
screen.fill((128, 255, 128))
pygame.draw.rect(screen, (50, 50, 50), (width/2-road_width/2, 0, road_width, height))
pygame.draw.rect(screen, (255, 255, 255), (width/2-roadmark/2, 0, roadmark, height))
pygame.draw.rect(screen, (255, 255, 255), (width/2-road_width/2 + roadmark*2, 0, roadmark, height))
pygame.draw.rect(screen, (255, 255, 255), (width/2+road_width/2 - roadmark*3, 0, roadmark, height))

pygame.display.update()

car1 = pygame.image.load("car_green.png")
car1_loc = car1.get_rect()
car1_loc.center = width/2 + road_width/4, height*0.8

car2 = pygame.image.load("car_red.png")
car2_loc = car2.get_rect()
car2_loc.center = width/2 - road_width/4, height*0.2


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(car1, car1_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()


pygame.quit()
