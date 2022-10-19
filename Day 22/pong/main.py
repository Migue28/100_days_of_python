from turtle import Screen, Turtle
from net import Net
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

ALIGNMENT = "center"
FONT_FAMILY = "Franklin Gothic"
FONT_SIZE = 25
FONT_TYPE = "normal"
FONT = (FONT_FAMILY, FONT_SIZE, FONT_TYPE)
MAX_SCORE = 10

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
r_scoreboard = Scoreboard(r_player.player_side, screen.window_height())
r_scoreboard.draw_score()
l_scoreboard = Scoreboard(l_player.player_side, screen.window_height())
l_scoreboard.draw_score()

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
        ball.increase_speed()

    # Detect paddle collision
    if ball.distance(r_player) < 50 and ball.xcor() > int(SCREEN_WIDTH/2)-50 \
            or ball.distance(l_player) < 50 and ball.xcor() < (int(SCREEN_WIDTH/2)-50)*-1:
        ball.bounce_x()
        ball.increase_speed()

    # Detect right wall collision
    if ball.xcor() > (int(SCREEN_WIDTH/2)-30):
        l_scoreboard.increase_score()
        l_scoreboard.clear()
        l_scoreboard.draw_score()
        ball.reset_ball_position()

    # Detect left wall collision
    if ball.xcor() < (int(SCREEN_WIDTH / 2) - 30) * -1:
        r_scoreboard.increase_score()
        r_scoreboard.clear()
        r_scoreboard.draw_score()
        ball.reset_ball_position()

    if r_scoreboard.score == MAX_SCORE or l_scoreboard.score == MAX_SCORE:
        game_on = False

game = Turtle()
game.hideturtle()
game.color("white")
game.penup()
game.write("GAME OVER", align=ALIGNMENT, font=FONT)

screen.exitonclick()
