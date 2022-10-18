from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)

    def level_up(self):
        self.level += 1

    def draw_score(self):
        self.clear()
        self.write(f"Level {self.level}", font=FONT)
