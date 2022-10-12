# import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

# colors = colorgram.extract('image.jpg', 20)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)

color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164)]

tim = Turtle()
screen = Screen()
colormode(255)
tim.speed(0)


def draw_square_dots(columns_number):
    y_position = -100
    tim.penup()
    tim.setposition(-100, y_position)

    def draw_rows(dots_number):
        for _ in range(dots_number):
            tim.color(choice(color_list))
            tim.dot(20)
            tim.penup()
            tim.forward(50)
            tim.pendown()
    for _ in range(columns_number):
        tim.pendown()
        draw_rows(columns_number)
        y_position += 50
        tim.penup()
        tim.setposition(-100, y_position)


draw_square_dots(10)
screen.exitonclick()
