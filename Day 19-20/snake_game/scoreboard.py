from turtle import Turtle
SCORE_COORDINATES = (0, 270)
ALIGNMENT = "center"
FONT_FAMILY = "Franklin Gothic"
FONT_SIZE = 15
FONT_TYPE = "normal"
FONT = (FONT_FAMILY, FONT_SIZE, FONT_TYPE)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.draw_score()

    def score_up(self):
        self.score += 1
        self.clear()
        self.draw_score()

    def draw_score(self):
        self.goto(SCORE_COORDINATES)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
