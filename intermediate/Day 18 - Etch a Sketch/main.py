from turtle import Turtle, Screen

class EtchASketch:
    def __init__(self):
        self.turtle = Turtle()
        self.screen = Screen()
        self.screen.listen()
        self.screen.onkeypress(key="Up", fun=self.move_forwards)
        self.screen.onkeypress(key="Right", fun=self.move_right)
        self.screen.onkeypress(key="Left", fun=self.move_left)
        self.screen.onkeypress(key="Down", fun=self.move_backwards)
        self.screen.onkeypress(key="c", fun=self.clear_screen)
        self.screen.exitonclick()

    def move_backwards(self):
        self.turtle.backward(10)

    def move_forwards(self):
        self.turtle.forward(10)

    def move_right(self):
        self.turtle.right(10)

    def move_left(self):
        self.turtle.left(10)

    def clear_screen(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()

if __name__ == "__main__":
    my_app = EtchASketch()