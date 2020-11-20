import turtle as t
import randomcolor


timmy_the_turtle = t.Turtle()
rand_color = randomcolor.RandomColor()

for i in range(4,9):
    color = rand_color.generate()[0];
    timmy_the_turtle.pencolor(color)
    for _ in range(i):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360/i)

screen = t.Screen()
screen.exitonclick()