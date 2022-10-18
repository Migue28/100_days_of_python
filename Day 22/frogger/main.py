import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_NUMBERS = 60
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
            cars[index].clear_car()
            cars.pop(index)
        if cars[index].distance(player) < 10:
            game_is_on = False
        if len(cars) < CAR_NUMBERS:
            cars.append(CarManager())
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.level_up()
        for car in cars:
            car.add_speed()

screen.exitonclick()


