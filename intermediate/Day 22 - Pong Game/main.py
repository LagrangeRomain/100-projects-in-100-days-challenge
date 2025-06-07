import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_HEIGHT, PADDLE_DISTANCE, PADDLE_WIDTH, BALL_WIDTH
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

screen.max_x = SCREEN_WIDTH // 2
screen.max_y = SCREEN_HEIGHT // 2

scoreboard = Scoreboard(screen.max_y)

paddle_position = screen.max_x - PADDLE_DISTANCE
paddle_r = Paddle(x=paddle_position, y=0)
paddle_l = Paddle(x=-paddle_position, y=0)

screen.onkeypress(key="Up", fun=paddle_r.go_up)
screen.onkeypress(key="Down", fun=paddle_r.go_down)
screen.onkeypress(key="z", fun=paddle_l.go_up)
screen.onkeypress(key="s", fun=paddle_l.go_down)

ball = Ball()
max_ball_y = screen.max_y - (ball.shapesize()[1]*20)
ball_contact_x = screen.max_x - PADDLE_DISTANCE - (PADDLE_WIDTH * 20)
max_paddle_distance = PADDLE_HEIGHT*20//2

game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    
    #Detect collision with walls
    if ball.ycor() <= -max_ball_y or ball.ycor() >= max_ball_y:
        ball.bounce_y()

    #Detect collision with paddles
    if (
            ball.distance(paddle_r) <= max_paddle_distance and ball.xcor() > ball_contact_x or
            ball.distance(paddle_l) <= max_paddle_distance and ball.xcor() < -ball_contact_x
    ):
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > screen.max_x - (BALL_WIDTH * 20):
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses
    if ball.xcor() < -(screen.max_x - (BALL_WIDTH * 20)):
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()