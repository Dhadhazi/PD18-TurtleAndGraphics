import turtle as t

import random

t.colormode(255)
timmy_the_turtle = t.Turtle()
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def random_walk():
    timmy_the_turtle.right(90*random.randint(0,4))
    timmy_the_turtle.pencolor(random_color())
    timmy_the_turtle.forward(25)

for i in range(150):
    random_walk()

screen = t.Screen()
screen.exitonclick()