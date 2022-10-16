from turtle import Turtle


class Net:
    def __init__(self):
        self.net = Turtle("square")
        self.net.color("white")
        self.net.turtlesize(0.5, 1, 1)
        self.net.penup()
        self.net.setposition(x=0, y=-300)
        self.net.left(90)

    def create_net(self, screen_height):
        """Create net for pong, request screen height"""
        for _ in range(int(screen_height / 2) * -1, int(screen_height / 2) + 1, 30):
            self.net.stamp()
            self.net.penup()
            self.net.forward(30)
            self.net.pendown()
