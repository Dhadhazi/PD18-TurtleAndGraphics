import turtle as t
import randomcolor
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed(0)
rand_color = randomcolor.RandomColor()

def random_walk():
    timmy_the_turtle.right(90*random.randint(0,4))
    timmy_the_turtle.pencolor(rand_color.generate()[0])
    timmy_the_turtle.forward(25)

for i in range(150):
    random_walk()

screen = t.Screen()
screen.exitonclick()