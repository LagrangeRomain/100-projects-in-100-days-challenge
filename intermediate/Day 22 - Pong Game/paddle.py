from turtle import Turtle
from config import PADDLE_SHAPE, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_COLOR

class Paddle(Turtle):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.teleport(x, y)
        self.penup()
        self.shape(PADDLE_SHAPE)
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH)
        self.color(PADDLE_COLOR)

    def go_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)