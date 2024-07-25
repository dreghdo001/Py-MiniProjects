import turtle
from turtle import Turtle, Screen, colormode
import random
import colorgram

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def extract_colors(path):
    """EXTRACTS COLORS FROM AN IMAGE THAT IT WAS GIVEN"""
    rgb_colors = []
    colors = colorgram.extract(f"{path}", 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rgb_colors.append(new_color)
    return rgb_colors

#colors = extract_colors("painting.jpg")
color_list= [[(186, 178, 180), (207, 195, 165), (145, 83, 60), (157, 177, 162), (159, 175, 183), (52, 107, 126), (56, 122, 94), (133, 70, 81), (210, 183, 178), (204, 184, 188), (166, 147, 57), (131, 33, 25), (71, 38, 28), (135, 27, 35), (191, 98, 81), (17, 94, 72), (177, 201, 189), (101, 145, 114), (21, 59, 76), (65, 35, 41), (184, 87, 96), (79, 147, 160), (16, 84, 99), (26, 64, 48), (186, 190, 200)]]

timmy = Turtle()
colormode(255)

screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
timmy.shape("turtle")
timmy.penup()
timmy.speed(0)
timmy.hideturtle()
for i in range(1,11):
    for j in range(10):
        timmy.dot(30, random_color())
        timmy.forward(50)
    timmy.goto(0,i*40)

screen.exitonclick()