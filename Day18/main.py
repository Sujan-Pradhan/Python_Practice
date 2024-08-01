import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
# timmy_the_turtle.forward(200)
# timmy_the_turtle.left(90)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(200)

# for _ in range(4):
#     timmy_the_turtle.forward(200)
#     timmy_the_turtle.left(90)


####### Draw dotted line ########    
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()



######## Draw different colors shapes ###############
# num_sides = 3
colours = ["blue", "green", "yellow", "orange", "black", "magenta", "cyan", "pink"]
# while num_sides < 11:
#     timmy_the_turtle.color(random.choice(colours))
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)   
#     num_sides += 1

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range (num_sides): 
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# for shape_side_n in range(3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)
        

# for _ in range(3):
#     timmy_the_turtle.color("blue")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(120)

# for _ in range(4):
#     timmy_the_turtle.color("green")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# for _ in range(5):
#     timmy_the_turtle.color("red")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(72)

# for _ in range(6):
#     timmy_the_turtle.color("deep pink")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(60)

# for _ in range(7):
#     timmy_the_turtle.color("dim gray")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(52)

# for _ in range(8):
#     timmy_the_turtle.color("green yellow")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(45)

# for _ in range(9):
#     timmy_the_turtle.color("magenta")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(40)

# for _ in range(10):
#     timmy_the_turtle.color("yellow")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(36)

#### Move turtle randomly ######
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r, g, b)
    
angles = [0,90,180,270]
for _ in range(200):
    timmy_the_turtle.pensize(20)
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.speed("fastest")
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(angles))

screen = t.Screen()
screen.exitonclick()