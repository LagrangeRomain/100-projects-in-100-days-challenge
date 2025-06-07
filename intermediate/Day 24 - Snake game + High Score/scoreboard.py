from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self, screen_width):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        y_position = screen_width // 2 - 30
        self.goto(0, y_position)
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} | High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.refresh_scoreboard()

    def save_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    def read_high_score(self):
        with open("data.txt", "r") as file:
            return int(file.read())