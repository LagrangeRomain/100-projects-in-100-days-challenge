from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, max_width, max_height):
        super().__init__()
        self.max_width = max_width
        self.max_height = max_height
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh_position()

    def refresh_position(self):
        random_x = random.randint(-self.max_width, self.max_width)
        random_y = random.randint(-self.max_height, self.max_height)
        self.goto(random_x, random_y)