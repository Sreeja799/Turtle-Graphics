from turtle import Turtle, Screen, bye
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle color will you bet on?")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

inc = 0
for i in colors:
    new = Turtle(shape = 'turtle')
    new.penup()
    new.color(i)
    new.goto(x=-230, y=-100+inc)
    inc += 50
    all_turtles.append(new)

end_of_race = False

while not end_of_race:
    for i in all_turtles:
        if i.xcor() > 230:
            winner = i.pencolor()
            if winner == user_bet:
                print(f'You have won the bet. {winner.title()} color won!')
            else:
                print(f'Sorry, you lost the bet. {winner.title()} color won!')
            end_of_race = True

        i.forward(randint(0, 10))

bye()
