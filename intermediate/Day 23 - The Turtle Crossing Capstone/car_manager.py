from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car(Turtle):
    def __init__(self, move_distance):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.setheading(180)
        random_color = random.choice(COLORS)
        self.color(random_color)
        random_y = random.randrange(-250,250,20)
        self.teleport(320, random_y)
        self.move_distance = move_distance

    def move_car(self):
        self.forward(self.move_distance)

    def increase_car_speed(self):
        self.move_distance += MOVE_INCREMENT

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        new_car = Car(self.move_distance)
        self.cars.append(new_car)

    def manage(self):
        spawn_threshold = max(1, 6 - self.move_distance // 5)
        random_chance = random.randint(0, spawn_threshold)
        if random_chance == 0:
            self.add_car()
        for car in self.cars:
            car.move_car()
        self.delete_car()

    def delete_car(self):
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)

    def increase_traffic_speed(self):
        self.move_distance += MOVE_INCREMENT
        for car in self.cars:
            car.move_distance = self.move_distance
