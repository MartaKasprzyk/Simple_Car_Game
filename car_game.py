import pygame
from pygame.locals import *

size = width, height = (800, 800)
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

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


pygame.quit()
