# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (186, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (195, 79, 72), (161, 201, 219), (45, 74, 77), (79, 74, 44), (57, 126, 122), (218, 175, 187), (168, 206, 169), (220, 182, 168)]

tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.speed("fastest")
tim.forward(300)
tim.left(135)


for i in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen.exitonclick()
