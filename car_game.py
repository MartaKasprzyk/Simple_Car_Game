import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_width = int(width / 1.6)
roadmark = int(width / 80)
right_lane = width / 2 + road_width / 4
left_lane = width / 2 - road_width / 4
speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MEK's car game")
screen.fill((128, 255, 128))

pygame.display.update()

car1 = pygame.image.load("car1.png")
car1_loc = car1.get_rect()
car1_loc.center = right_lane, height * 0.8

car2 = pygame.image.load("car2.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

rock = pygame.image.load("rock.png")
rock_loc = rock.get_rect()
rock_loc.center = width / 8, height * 0.8

bush = pygame.image.load("bush.png")
bush_loc = bush.get_rect()
bush_loc1 = bush.get_rect()
bush_loc.center = width * 0.9, height * 0.2
bush_loc1.center = width * 0.9, height * 0.6

counter = 0

font = pygame.font.SysFont('arial', 36)
text = font.render('GAME OVER', True, (255, 255, 255))
text_loc = text.get_rect()
text_loc.center = width / 2, height / 2

game_over_sound = pygame.mixer.Sound("sound of your choice")

while running:
    counter += 1
    if counter == 1000:
        speed += 0.5
        counter = 0
        print("level up", speed)
    car2_loc[1] += speed
    rock_loc[1] += speed
    bush_loc[1] += speed
    bush_loc1[1] += speed
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
            rock_loc.center = width / 8, height * 0.2
        else:
            car2_loc.center = left_lane, -200
            rock_loc.center = width / 8, height * 0.8
            bush_loc.center = width * 0.9, -100
            bush_loc1.center = width * 0.9, -300

    if car1_loc[0] == car2_loc[0] and car2_loc[1] > car1_loc[1] - 250:
        screen.fill((0, 0, 0))
        screen.blit(text, text_loc)
        pygame.display.update()
        game_over_sound.play()
        pygame.time.wait(600)
        print("GAME OVER!")
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car1_loc = car1_loc.move([-int(road_width / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car1_loc = car1_loc.move([int(road_width / 2), 0])

    pygame.draw.rect(screen, (128, 255, 128), (width / 4 - road_width / 2, 0, road_width, height))
    pygame.draw.rect(screen, (128, 255, 128), (width / 4 + road_width / 2, 0, road_width, height))
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_width / 2, 0, road_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - roadmark / 2, 0, roadmark, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_width / 2 + roadmark * 2, 0, roadmark, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_width / 2 - roadmark * 3, 0, roadmark, height))

    screen.blit(rock, rock_loc)
    screen.blit(bush, bush_loc)
    screen.blit(bush, bush_loc1)
    screen.blit(car1, car1_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()

pygame.quit()
