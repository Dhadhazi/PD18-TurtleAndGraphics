import turtle as t

import random

t.colormode(255)
timmy_the_turtle = t.Turtle()
timmy_the_turtle.pensize(1)
timmy_the_turtle.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_circle():
    timmy_the_turtle.pencolor(random_color())
    timmy_the_turtle.circle(100)

for _ in range(90):
    draw_circle()
    timmy_the_turtle.right(4)

screen = t.Screen()
screen.exitonclick()