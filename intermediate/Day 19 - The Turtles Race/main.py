from turtle import Turtle, Screen
import random

class TurtleRace:
    def __init__(self, screen_width=1000, screen_height=400):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.is_race_on = False
        self.screen = Screen()
        self.screen.setup(width=screen_width, height=screen_height)
        self.user_bet = self.screen.textinput("Make your bet", "Place your bet on the winning turtle. Enter a color: ")
        self.turtles = []
        self.draw_finish_line()
        self.create_and_place_turtles()


    def create_and_place_turtles(self):
        y_position = -100
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]

        for color in colors:
            new_turtle = Turtle()
            new_turtle.shape("turtle")
            new_turtle.color(color)
            new_turtle.penup()
            new_turtle.goto(x=-((self.screen_width/2)-20), y=y_position)
            y_position += 40
            self.turtles.append(new_turtle)

    def draw_finish_line(self):
        line = Turtle()
        line.hideturtle()
        line.penup()
        line.goto((self.screen_width / 2) - 20, -self.screen_height / 2)
        line.pendown()
        line.left(90)
        line.forward(self.screen_height)

    def start_race(self):
        self.is_race_on = True
        while self.is_race_on:
            for turtle in self.turtles:
                random_distance = random.randint(0,10)
                turtle.forward(random_distance)
                turtle_position = turtle.xcor()
                if turtle_position >= (self.screen_width/2)-20:
                    winning_turtle = turtle.pencolor()
                    if self.user_bet == winning_turtle:
                        print(f"You've won ! The {winning_turtle} turtle is the winner!")
                    else:
                        print(f"You've lost ! The {winning_turtle} turtle is the winner!")
                    self.is_race_on = False
        self.screen.exitonclick()

turtle_race = TurtleRace()
turtle_race.start_race()