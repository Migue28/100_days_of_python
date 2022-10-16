from turtle import Screen
from net import Net
from player import Player

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
SCREEN_TITLE = "PONG!"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)
player1 = Player("left")
player2 = Player("right")

player1.draw_player(SCREEN_WIDTH)
player2.draw_player(SCREEN_WIDTH)
net = Net()
net.create_net(SCREEN_HEIGHT)
screen.update()

screen.exitonclick()
