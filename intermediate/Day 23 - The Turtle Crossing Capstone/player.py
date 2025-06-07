from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.refresh_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def refresh_position(self):
        self.goto(STARTING_POSITION)

    def has_cross_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.refresh_position()
            return True
        else:
            return False