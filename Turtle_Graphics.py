from turtle import *

my_turtle = Turtle()
my_screen = Screen()

bgcolor("gold")
my_turtle.shape("turtle")
my_turtle.color("PaleGreen4")
my_turtle.pencolor('DeepPink4')
my_turtle.pensize(2)
my_turtle.speed(10)

while True:
    my_turtle.forward(200)
    my_turtle.left(170)
    my_turtle.stamp()
    if abs(my_turtle.pos()) < 1:
        break

end_fill()
my_screen.exitonclick()