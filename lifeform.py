import random


class LifeForm:
    def __init__(self, color):
        self.fed = False
        self.food_seen = False
        self.color = color
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

        self.width = 40
        self.height = 40
        self.vel = 10

    def move(self):
        left = 2
        right = 2
        up = 2
        down = 2
        if self.x < 250 and self.y < 250:
            down, right = 4, 4
        elif self.x < 250 and self.y > 250:
            up, right = 4, 4
        elif self.x > 250 and self.y < 250:
            down, left = 4, 4
        elif self.x > 250 and self.y > 250:
            up, left = 4, 4

        if not self.fed and not self.food_seen:
            pass
        dir = random.randint(1, 12)
        if 1 <= dir <= left and self.x > 0:
            self.x -= self.vel
        if left <= dir <= left + right and self.x < 500 - self.width:
            self.x += self.vel
        if left + right <= dir <= left + right + up and self.y > 0:
            self.y -= self.vel
        if left + right + up <= dir <= left + right + up + down and self.y < 500 - self.height:
            self.y += self.vel
        return self.x, self.y, self.width, self.height
