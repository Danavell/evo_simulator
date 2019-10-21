import random

import pygame

import EventHandlers as e
from lifeform import Food

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Evolution Simulator')

x = 50
y = 460
width = 40
height = 40
vel = 10

life_forms = e.create_life()

num_tries = 10
current_try = 0
while num_tries >= current_try:
    current_try += 1
    food_life_form_dict = dict()
    food_list = list()
    amount_of_food = random.randint(1, 30)
    for i in range(amount_of_food):
        food_list.append(Food(id=i))
        food_life_form_dict[i] = list()

    life_forms = e.successive_round(
        win=win,
        life_forms=life_forms,
        food_list=food_list,
        food_life_form_dict=food_life_form_dict
    )
    for life in life_forms:
        life.fed = False
        life.end_point = None
pygame.quit()

