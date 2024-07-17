from turtle import Turtle, Screen, colormode
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color




timmy = Turtle()
timmy.shape("turtle")
colormode(255)
timmy.speed(0)

def draw_spinograph(size):
    angle = 0
    for _ in range(100):
        while angle <= 360:
            timmy.color(random_color())
            timmy.circle(100)
            timmy.right(size)
            angle +=size


draw_spinograph(5)

screen = Screen()
screen.exitonclick()