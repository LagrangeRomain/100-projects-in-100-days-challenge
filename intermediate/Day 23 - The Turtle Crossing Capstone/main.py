import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun= player.move)
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.manage()
    if player.has_cross_line():
        car_manager.increase_traffic_speed()
        scoreboard.increase_score()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()