from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_position()


    def refresh_position(self):
        min_width = int(-(self.screen_width / 2) + 20)
        max_width = int((self.screen_width / 2) - 20)
        min_height = int(-(self.screen_height / 2) + 20)
        max_height = int((self.screen_height / 2) - 20)
        random_x = random.randint(min_width, max_width)
        random_y = random.randint(min_height, max_height)
        self.goto(random_x, random_y)