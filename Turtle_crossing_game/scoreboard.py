import time
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.clear()
        self.color("black")
        self.penup()
        self.goto(-250,250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Arial", 22, "normal"))

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over !",align="center", font=("Arial", 22, "normal"))

        time.sleep(5)