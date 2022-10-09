from turtle import Turtle, Screen
import prettytable

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.resizemode("auto")
timmy.color("gold4")
timmy.forward(100)
timmy.right(-90)
timmy.forward(-100)

my_screen = Screen()
print(my_screen.canvheight, my_screen.canvwidth)
my_screen.exitonclick()
