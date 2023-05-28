import turtle as t
from random import randint, choice

t.colormode(255)
tim = t.Turtle()
tim.pensize(10)
tim.speed(10)
screen = t.Screen()

directions = [0, 90, 180, 270]


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


for _ in range(200):
    tim.pencolor(random_colour())
    tim.forward(30)
    tim.setheading(choice(directions))

screen.exitonclick()
