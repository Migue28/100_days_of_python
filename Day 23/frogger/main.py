import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_NUMBERS = 20
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkeypress(fun=player.move, key="Up")

cars = []
for _ in range(CAR_NUMBERS):
    cars.append(CarManager())

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.draw_score()
    for index in range(len(cars)-1):
        cars[index].move_car()
        if cars[index].xcor() < -320:
            cars[index].starting_position()
        if cars[index].distance(player) < 20:
            game_is_on = False
        if len(cars) < CAR_NUMBERS:
            cars.append(CarManager())
    if player.ycor() == FINISH_LINE_Y:
        scoreboard.level_up()
        player.reset_position()
        for car in cars:
            car.add_speed()
        print(cars[0].speed())
screen.update()
scoreboard.game_over()

screen.exitonclick()


