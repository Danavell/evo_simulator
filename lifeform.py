import random


class LifeForm:
    def __init__(self, color):
        self.color = color
        self.x = 50
        self.y = 460
        self.width = 40
        self.height = 40
        self.vel = 10

    def move(self):
        dir = random.randint(1, 12)
        if 1 <= dir <= 3 and self.x > 0:
            self.x -= self.vel
        if 4 <= dir <= 6 and self.x < 500 - self.width:
            self.x += self.vel
        if 7 <= dir <= 9 and self.y > 0:
            self.y -= self.vel
        if 10 <= dir <= 12 and self.y < 500 - self.height:
            self.y += self.vel
        return self.x, self.y, self.width, self.height
