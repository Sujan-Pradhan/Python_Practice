import turtle as t
import random

timmy_turtle = t.Turtle()
timmy_turtle.shape("turtle")

t.colormode(255)

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return (r,g,b)

timmy_turtle.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):

        timmy_turtle.color(random_color())
        timmy_turtle.circle(200,360)
        current_heading = timmy_turtle.heading()
        timmy_turtle.setheading(current_heading+size_of_gap)
        # timmy_turtle.circle(100,360)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()