import time
from turtle import Screen
from players import Player
from ball import Ball
import random

DIRECTIONS = [45, 135,225,315]

# Set screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Player((350,0))
l_paddle = Player((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")
screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()






screen.exitonclick()