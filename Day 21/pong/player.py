from turtle import Turtle


class Player:
    def __init__(self, player_side):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.left(90)
        self.paddle.turtlesize(stretch_len=3)
        self.player_side = player_side
        self.paddle.penup()

    def draw_player(self, screen_width):
        """Create the player, request screen width."""
        if self.player_side == 'right':
            self.paddle.setposition(x=int(screen_width / 2) - 20, y=0)
        else:
            self.paddle.setposition(x=int((screen_width / 2) - 10)*-1, y=0)

    def move_up(self):
        self.paddle.forward(20)

    def move_down(self):
        self.paddle.forward(-20)
