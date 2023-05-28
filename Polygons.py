from turtle import Screen, Turtle
import random

tim = Turtle()
tim.penup()
tim.left(90)
tim.forward(150)
tim.right(90)
tim.pendown()
tim.speed(10)
screen = Screen()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(3, 11):
    tim.color(random.choice(colors))
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)

screen.exitonclick()
