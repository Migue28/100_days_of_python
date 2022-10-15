from turtle import Screen
import time
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE!")
screen.tracer(0)
snake = Snake()
food = Food()

# Controls
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.reappear()

screen.exitonclick()
