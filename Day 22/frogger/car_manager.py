from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.penup()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.left(180)
        self.starting_position()
        self.turtlesize(stretch_wid=1, stretch_len=2)

    def move_car(self):
        self.forward(self.car_speed)

    def add_speed(self):
        self.car_speed += MOVE_INCREMENT

    def starting_position(self):
        x_pos = randint(280, 880)
        y_pos = randint(-250, 260)
        self.goto(x_pos, y_pos)

    def clear_car(self):
        self.hideturtle()
