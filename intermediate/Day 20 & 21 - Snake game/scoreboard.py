from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self, screen_width):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        y_position = screen_width // 2 - 30
        self.goto(0, y_position)

        self.score = 0
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
