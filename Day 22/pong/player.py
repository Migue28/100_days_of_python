from turtle import Turtle


class Player(Turtle):
    def __init__(self, player_side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.left(90)
        self.turtlesize(stretch_len=5)
        self.player_side = player_side
        self.penup()

    def draw_player(self, screen_width):
        """Create the player, request screen width."""
        if self.player_side == 'right':
            self.setposition(x=int(screen_width / 2) - 30, y=0)
        else:
            self.setposition(x=int((screen_width / 2) - 30)*-1, y=0)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.forward(-20)
