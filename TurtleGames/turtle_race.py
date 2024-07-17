from turtle import Turtle, Screen
from tkinter import messagebox
import random

screen = Screen()
screen.setup(width=500,height=400)
screen.bgcolor("#AED6F1")

colors=["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the game : Enter a color?")

y_position=[-80, -40, 0, 40, 80, 120]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo("Result", f"You win ! The {winning_color} is the winner !")
                break
            else:
                messagebox.showinfo("Result", f"You've lost ! The {winning_color} is the winner !")
                break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)













screen.listen()
screen.exitonclick()