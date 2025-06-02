from turtle import Turtle, Screen
import random

def randomize_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb_value = (r,g,b)
    return rgb_value

def do_art(turtle, window):
    turtle.forward(50)
    color = randomize_color()
    turtle.dot(20, color)

screen = Screen()
screen.colormode(255)
screen.setup(height=500, width=500)

tim = Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
tim.goto(-250, -200)

for _ in range (9):
    tim.setheading(0)
    for _ in range(9):
        do_art(tim, screen)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(450)

screen.exitonclick()