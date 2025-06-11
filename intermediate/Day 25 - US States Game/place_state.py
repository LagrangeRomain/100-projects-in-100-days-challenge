from turtle import Turtle

class PlaceState(Turtle):
    def __init__(self, state, x, y, color):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(color)
        self.goto(x, y)
        self.write(state)
