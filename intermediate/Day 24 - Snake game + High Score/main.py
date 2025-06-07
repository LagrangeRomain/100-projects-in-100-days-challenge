from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


screen = Screen()
scoreboard = Scoreboard(SCREEN_WIDTH)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
max_width = SCREEN_WIDTH // 2 - snake.segment_size
max_height = SCREEN_HEIGHT // 2 - snake.segment_size
print(-max_width, -max_height)
food = Food(max_width, max_height)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_position()
        snake.grow()
        scoreboard.increase_score()

    #Detect collision with walls
    if (
        snake.head.xcor() > max_width or
        snake.head.xcor() < -max_width or
        snake.head.ycor() > max_height or
        snake.head.ycor() < -max_height
    ):
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()