from turtle import Turtle
from config import BALL_SHAPE, BALL_HEIGHT, BALL_WIDTH, BALL_COLOR, BALL_STEPS

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(BALL_SHAPE)
        self.shapesize(BALL_HEIGHT, BALL_WIDTH)
        self.color(BALL_COLOR)
        self.setheading(45)
        self.x_step = BALL_STEPS
        self.y_step = BALL_STEPS
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_step *= -1

    def bounce_x(self):
        print("bounce")
        self.x_step *= -1
        self.speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.speed = 0.1