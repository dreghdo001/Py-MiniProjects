import threading
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()

screen.listen()

cars = []
screen.onkey(player.move_up, "Up")
game_is_on = True
index = 0
while game_is_on:
    time.sleep(0.1)
    if index % 5 ==0:
        cars.append(CarManager())
    index +=1
    for car in cars:
        if player.distance(car) < 25:
            player.increase_level()
            car.increase_level()
        if player.ycor() >= 280:
            score.increase_score()
            player.increase_level()
            car.increase_level()

        car.move()
    screen.update()



