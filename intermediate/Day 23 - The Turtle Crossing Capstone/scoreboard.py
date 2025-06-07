from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-290,270)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Level : {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=FONT)