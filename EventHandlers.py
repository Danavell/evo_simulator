import math
import operator
import random

import pygame

from lifeform import LifeForm


def create_life():
    life_forms = [
        LifeForm(color=(255, 0, 0)),
        LifeForm(color=(127, 0, 0)),
        LifeForm(color=(0, 255, 0)),
        LifeForm(color=(0, 127, 0)),
        LifeForm(color=(0, 0, 255)),
        LifeForm(color=(0, 0, 127)),
        LifeForm(color=(255, 255, 255)),
        LifeForm(color=(127, 127, 127)),
    ]

    for i in range(len(life_forms)):
        life_forms[i].id = i
    return life_forms


def successive_round(win, life_forms, food_list, food_life_form_dict):
    num_tries = 100
    current_try = 0
    run = True
    while run:
        current_try += 1
        if current_try == num_tries:
            run = False
            continue
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((0, 0, 0))
        for food in food_list:
            if not food.eaten:
                pygame.draw.circle(win, (255, 255, 255), (food.x, food.y), 5)

        for life in life_forms:
            potential_food = list()
            for food in food_list:
                x_diff = life.x - food.x
                y_diff = life.y - food.y
                distance_to_food = math.sqrt(y_diff ** 2 + x_diff ** 2)
                if life.vision > distance_to_food:
                    potential_food.append((food, distance_to_food))
            if len(potential_food) == 1:
                food_life_form_dict[potential_food[0][0].id].append(life)
                life.target_food = potential_food[0][0]
            elif len(potential_food) > 1:
                potential_food.sort(key=operator.itemgetter(1), reverse=False)

                present = False
                for life_form in food_life_form_dict[potential_food[0][0].id]:
                    if life.id == life_form.id:
                        present = True
                if not present:
                    food_life_form_dict[potential_food[0][0].id].append(life)
                life.target_food = potential_food[0][0]
            pygame.draw.circle(win, life.color, move(life), 20)

            if life.target_food:
                x_diff = life.x - life.target_food.x
                y_diff = life.y - life.target_food.y
                distance_to_food = math.sqrt(x_diff ** 2 + y_diff ** 2)

                if life.radius >= distance_to_food:
                    id = life.target_food.id
                    subscribers = food_life_form_dict.get(life.target_food.id)
                    for subscriber in subscribers:
                        subscriber.target_food = None

                    food_life_form_dict[id] = list()

                    temp_food = list()
                    for food in food_list:
                        if food.id != id:
                            temp_food.append(food)
                    food_list = temp_food
                    life.fed = True
            if num_tries - current_try == 1:
                temp_life = list()
                for life in life_forms:
                    if life.x - life.radius == 0 or life.x + life.radius == 500 or life.y - life.radius == 0 or life.y + life.radius == 500:
                        temp_life.append(life)
                life_forms = temp_life

        pygame.display.update()
    return life_forms


def move(life):
    if not life.fed and not life.target_food:
        left, right, up, down = 2, 2, 2, 2
        if life.x < 250 and life.y < 250:
            down, right = 4, 4
        elif life.x < 250 and life.y > 250:
            up, right = 4, 4
        elif life.x > 250 and life.y < 250:
            down, left = 4, 4
        elif life.x > 250 and life.y > 250:
            up, left = 4, 4

        dir = random.randint(1, 12)
        if 1 <= dir <= left and life.x > 0:
            life.x -= life.vel
        if left <= dir <= left + right and life.x < 500 - life.radius:
            life.x += life.vel
        if left + right <= dir <= left + right + up and life.y > 0:
            life.y -= life.vel
        if left + right + up <= dir <= left + right + up + down and life.y < 500 - life.radius:
            life.y += life.vel

    if not life.fed and life.target_food:
        movements = [
            (-life.vel, 0),
            (life.vel, 0),
            (0, -life.vel),
            (0, life.vel)
        ]
        outcomes = list()

        for movement in movements:
            x_diff = life.x + movement[0] - life.target_food.x
            y_diff = life.y + movement[1] - life.target_food.y
            distance_to_food = math.sqrt(y_diff**2 + x_diff**2)
            outcomes.append((movement, distance_to_food))

        outcomes.sort(key=operator.itemgetter(1), reverse=False)
        life.x += outcomes[0][0][0]
        life.y += outcomes[0][0][1]

    if life.fed:
        if not life.end_point:
            potential_locations = [
                ('left', life.x - life.radius),
                ('right', 500 - life.x + life.radius),
                ('up', life.y - life.radius),
                ('down', 500 - life.y + life.radius)
            ]
            potential_locations.sort(key=operator.itemgetter(1), reverse=False)
            life.end_point = potential_locations[0][0]

        else:
            if life.end_point == 'left':
                if life.x - life.radius > 0:
                    life.x -= life.vel
            if life.end_point == 'right':
                if life.x + life.radius < 500:
                    life.x += life.vel
            if life.end_point == 'up':
                if life.y - life.radius > 0:
                    life.y -= life.vel
            if life.end_point == 'down':
                if life.y + life.radius < 500:
                    life.y += life.vel

    return life.x, life.y
