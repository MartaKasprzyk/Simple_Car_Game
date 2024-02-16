import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_width = int(width/1.6)
roadmark = int(width/80)
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MEK's car game")
screen.fill((128, 255, 128))


pygame.display.update()

car1 = pygame.image.load("car1.png")
car1_loc = car1.get_rect()
car1_loc.center = right_lane, height*0.8

car2 = pygame.image.load("car2.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2


while running:
    car2_loc[1] += 1
    if car2_loc[1] > height:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car1_loc = car1_loc.move([-int(road_width/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car1_loc = car1_loc.move([int(road_width/2), 0])

    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_width / 2, 0, road_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - roadmark / 2, 0, roadmark, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_width / 2 + roadmark * 2, 0, roadmark, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_width / 2 - roadmark * 3, 0, roadmark, height))

    screen.blit(car1, car1_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()


pygame.quit()
