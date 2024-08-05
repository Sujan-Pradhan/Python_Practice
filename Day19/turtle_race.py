from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet.", prompt= "Which turtle will win the race? Enter the color: ")
print(user_bet)

colors= ["red", "green", "yellow", "blue", "purple", "orange"]
y_positions = [-100, -60, -20, 20,60,100]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -280, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()