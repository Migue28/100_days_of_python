from turtle import Turtle

ALIGNMENT = "center"
FONT_FAMILY = "Franklin Gothic"
FONT_SIZE = 25
FONT_TYPE = "normal"
FONT = (FONT_FAMILY, FONT_SIZE, FONT_TYPE)


class Scoreboard(Turtle):
    def __init__(self, player_side, screen_height):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.player_side = player_side
        self.screen_height = screen_height

    def draw_score(self):
        if self.player_side == "right":
            self.goto(50, int(self.screen_height/2)-50)
            self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
        else:
            self.goto(-50, int(self.screen_height / 2) - 50)
            self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
