from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def clockwise():
    tim.right(10)


def anti_clockwise():
    tim.left(10)


screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=clockwise)
screen.onkey(key="D", fun=anti_clockwise)
screen.onkey(key='C', fun=clear)

screen.exitonclick()
