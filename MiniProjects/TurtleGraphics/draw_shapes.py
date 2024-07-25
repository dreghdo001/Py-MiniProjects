from turtle import Turtle, Screen, colormode
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def dashed_line(turtle, size):
    for _ in range(10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def draw_shape(turtle, num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        turtle.forward(100)
        turtle.right(angle)


timmy = Turtle()
colormode(255)
timmy.shape("turtle")


for _ in range(3,11):
    timmy.color(random_color())
    draw_shape(timmy, _)











screen = Screen()

screen.exitonclick()