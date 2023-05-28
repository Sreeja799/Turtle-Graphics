import turtle as t
from random import randint

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
screen = t.Screen()


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

def spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.pencolor(random_colour())
        tim.circle(100)
        tim.left(gap_size)

spirograph(5)
screen.exitonclick()
