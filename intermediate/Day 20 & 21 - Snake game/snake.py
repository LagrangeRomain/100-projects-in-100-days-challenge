from turtle import Turtle

SEGMENT_SIZE = 20
STARTING_SEGMENTS = 3
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake with STARTING_SEGMENTS segments."""
        x_position = 0
        for _ in range(STARTING_SEGMENTS):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x_position, 0)
            x_position -= SEGMENT_SIZE
            self.segments.append(new_segment)

    def move(self):
        """Move the snake forward by updating each segment's position to the one before it."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(SEGMENT_SIZE)

    def can_turn(self, new_heading):
        """Prevent the snake from reversing directly onto itself."""
        return abs(self.head.heading() - new_heading) != 180

    def up(self):
        if self.can_turn(UP) :
            self.head.setheading(UP)

    def down(self):
        if self.can_turn(DOWN):
            self.head.setheading(DOWN)

    def left(self):
        if self.can_turn(LEFT):
            self.head.setheading(LEFT)

    def right(self):
        if self.can_turn(RIGHT):
            self.head.setheading(RIGHT)