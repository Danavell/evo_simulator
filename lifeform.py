import random


class Food:
    def __init__(self, id):
        self.id = id
        self.x = random.randint(40, 460)
        self.y = random.randint(40, 460)
        self.radius = 5
        self.eaten = False


class LifeForm:
    def __init__(self, color, vision=40):
        self.id = None
        self.fed = False
        self.color = color
        self.vision = vision
        self.target_food = None
        self.vel = 10
        self.radius = 20
        self.end_point = None

        self.x = 0
        trigger = random.randint(1, 2)
        if trigger == 1:
            self.y = random.randint(0, 460)
            trigger = random.randint(1, 2)
            if trigger == 1:
                self.x = 0
            else:
                self.x = 460
        else:
            self.x = random.randint(0, 460)
            trigger = random.randint(1, 2)
            if trigger == 1:
                self.y = 0
            else:
                self.y = 460