import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)

game_map = turtle.shape(image)
data = pd.read_csv("50_states.csv")
# print(data)
game_is_on = True
user_points = 0
while game_is_on:
    user_state = screen.textinput(f"{user_points}/{len(data)} States Correct", "What's another state name?")
    for state in data.state:
        if state.lower() == user_state.lower():
            # print(f"{state} x: {data[data.state == state].x.item()} y: {data[data.state == state].y.item()}")
            user_points += 1
            state_name = turtle.Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_name.goto(int(data.x[data.state == state].item()), int(data.y[data.state == state].item()))
            state_name.write(state)
            # screen.update()
            break
    if user_points == len(data):
        game_is_on = False
screen.exitonclick()
