from turtle import Turtle
with open("data.txt") as file:
    high_score = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score : {self.high_score} ", align="center", font=("Arial", 22, "normal"))

    """
        def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over !", align="center", font=("Arial", 22, "normal"))
    """

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file2:
                file2.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

