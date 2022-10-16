from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 1

    def move(self):
        new_x = self.xcor() + self.x_move*self.speed
        new_y = self.ycor() + self.y_move*self.speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        self.y_move *= 1.1
        self.x_move *= 1.1

    def reset_ball_position(self):
        self.home()
        self.speed = 1
        self.x_move = 10
        self.y_move = 10
        self.bounce_x()
