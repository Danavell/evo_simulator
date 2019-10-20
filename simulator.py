import pygame
import random

from lifeform import LifeForm
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Evolution Simulator')

x = 50
y = 460
width = 40
height = 40
vel = 10

life_forms = [
    LifeForm(color=(255, 0, 0)),
    LifeForm(color=(0, 255, 0)),
    LifeForm(color=(0, 0, 255)),
    LifeForm(color=(255, 255, 255)),
]

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    for life in life_forms:
        pygame.draw.rect(win, life.color, life.move())
    pygame.display.update()

pygame.quit()

