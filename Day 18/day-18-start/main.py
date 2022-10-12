from turtle import Turtle, Screen, colormode
from random import randint, choice

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
colormode(255)

# Square
# for _ in range(4):
#     timmy.fd(100)
#     timmy.right(90)

# Dash Line
# for _ in range(4):
#     timmy.fd(50)
#     timmy.pu()
#     timmy.fd(50)
#     timmy.pd()


# angle art
# def angle_art(sides):
#     angle = 360 / sides
#     timmy.pencolor(randint(1, 256), randint(1, 256), randint(1, 256))
#     for _ in range(sides):
#         timmy.fd(100)
#         timmy.right(angle)
#
#
# for _sides in range(3, 10):
#     angle_art(_sides)


angle_list = [0, 90, 180, 270]


# Random walk
# def random_walk(steps_number):
#     timmy.pensize(15)
#     timmy.speed(0)
#     for _ in range(steps_number):
#         timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#         timmy.fd(20)
#         timmy.right(choice(angle_list))
#
#
# random_walk(1000)


# Spirograph
def spirograph(steps_number):
    angle = 360/steps_number
    timmy.speed(0)
    for _ in range(steps_number):
        timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.circle(100)
        timmy.right(angle)


spirograph(60)
screen = Screen()
screen.exitonclick()
