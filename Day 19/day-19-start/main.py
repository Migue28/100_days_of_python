from turtle import Screen
from commands import Tim

red = Tim()
orange = Tim()
blue = Tim()
yellow = Tim()
purple = Tim()
green = Tim()

turtles = [red, orange, blue, yellow, purple, green]

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.\
    textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? Enter a color: ")
user_bet.lower()
colors = ["red", "orange", "blue", "yellow", "purple", "green"]
x = -200
y = -100
for index in range(len(colors)):
    turtles[index].paint_turtle(colors[index])
    turtles[index].go_to_position(x_value=x, y_value=y)
    y += 50

turtle_won = False
while not turtle_won:
    winner = ""
    for turtle in turtles:
        turtle.race()
        if turtle.get_position() > 230:
            turtle_won = True
            winner = turtle.get_color()
            winner.lower()
if winner == user_bet:
    print(f"YOU WON. The {winner} turtle is the winner!")
else:
    print(f"You lost. The {winner} turtle is the winner")
# Sketch program
# screen.listen()
# screen.onkey(key="w", fun=tim.move_forward)
# screen.onkey(key="s", fun=tim.move_backward)
# screen.onkey(key="d", fun=tim.move_clockwise)
# screen.onkey(key="a", fun=tim.move_counter_clockwise)
# screen.onkey(key="c", fun=tim.reset_movement)
screen.exitonclick()
