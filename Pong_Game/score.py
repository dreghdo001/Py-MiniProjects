from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.score}", align="center", font=("Arial", 22, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over !", align="center", font=("Arial", 22, "normal"))
    def increase_score(self):
        self.clear()
        self.score +=1
        self.update_scoreboard()