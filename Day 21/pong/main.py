from turtle import Screen
from net import Net
from player import Player
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
SCREEN_TITLE = "PONG!"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

# Create the players
l_player = Player("left")
r_player = Player("right")
l_player.draw_player(SCREEN_WIDTH)
r_player.draw_player(SCREEN_WIDTH)

net = Net()
net.create_net(SCREEN_HEIGHT)
game_on = True

ball = Ball()

# Controls
screen.listen()
screen.onkeypress(fun=l_player.move_up, key="w")
screen.onkeypress(fun=r_player.move_up, key="Up")
screen.onkeypress(fun=l_player.move_down, key="s")
screen.onkeypress(fun=r_player.move_down, key="Down")

while game_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    # Detect vertical wall collision
    if ball.ycor() > int(SCREEN_HEIGHT/2)-20 or ball.ycor() < int(SCREEN_HEIGHT/-2)+20:
        ball.bounce_y()

    # Detect paddle collision
    if ball.distance(r_player) < 50 and ball.xcor() > int(SCREEN_WIDTH/2)-50 \
            or ball.distance(l_player) < 50 and ball.xcor() < (int(SCREEN_WIDTH/2)-50)*-1:
        ball.bounce_x()


screen.exitonclick()
