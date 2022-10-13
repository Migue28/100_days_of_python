from turtle import Turtle
from random import randint


class Tim:
    def __init__(self):
        self.tim = Turtle()
        self.tim.shape("turtle")
        self.tim.penup()

    def move_forward(self, speed):
        self.tim.forward(10*speed)

    def move_backward(self):
        self.tim.forward(-10)

    def move_clockwise(self):
        self.tim.right(10)

    def move_counter_clockwise(self):
        self.tim.right(-10)

    def reset_movement(self):
        self.tim.reset()

    def go_to_position(self, x_value, y_value):
        self.tim.goto(x=x_value, y=y_value)

    def paint_turtle(self, color):
        self.tim.color(color)

    def race(self):
        speed = randint(0, 10)*0.1
        self.move_forward(speed)

    def get_position(self):
        position = self.tim.position()
        return position[0]

    def get_color(self):
        color = self.tim.color()
        return color[0]
