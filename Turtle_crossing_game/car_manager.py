from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(x=250, y=random.randrange(-250, 250, 50))
        self.setheading(180)
        self.speed_level = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.speed_level)
    def increase_level(self):

        self.speed_level = self.speed_level + MOVE_INCREMENT

