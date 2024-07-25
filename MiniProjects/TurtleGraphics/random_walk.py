from turtle import Turtle, Screen, colormode
import random


def random_walk(turtle):
    directions = [0,90,180,270]
    random_way = random.choice(directions)
    turtle.forward(30)
    turtle.setheading(random_way)
    turtle.forward(30)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy = Turtle()
timmy.shape("turtle")
colormode(255)
timmy.pensize(15)
timmy.shapesize(1, 1, 6)
timmy.speed(0)

while True:
    timmy.color(random_color())
    random_walk(timmy)

screen = Screen()
screen.exitonclick()
