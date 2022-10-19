from turtle import Turtle
from random import randint
STRETCH_DIMENSIONS = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=STRETCH_DIMENSIONS, stretch_wid=STRETCH_DIMENSIONS)
        self.color("yellow")
        self.speed("fastest")
        self.reappear()

    def reappear(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x=random_x, y=random_y)
