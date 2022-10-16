from turtle import Turtle, Screen
from net import Net

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
SCREEN_TITLE = "PONG!"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)
net = Net()
net.create_net(SCREEN_HEIGHT)

screen.exitonclick()
