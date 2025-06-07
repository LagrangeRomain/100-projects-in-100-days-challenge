from turtle import Turtle
from config import SCOREBOARD_COLOR, SCOREBOARD_FONT

class Scoreboard(Turtle):
    def __init__(self, max_height):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.y = max_height-100
        self.update_scoreboard()

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, self.y)
        self.write(self.l_score, align="center", font=SCOREBOARD_FONT)
        self.goto(100, self.y)
        self.write(self.r_score, align="center", font=SCOREBOARD_FONT)