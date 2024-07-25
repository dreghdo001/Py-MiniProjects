from turtle import Turtle
PLAYER1_STARTING_POSITION = [(-380, 0), (-380, 20), (-380, 40)]
PLAYER2_STARTING_POSITION = [(380, 0), (380, 20), (380, 40)]

UP=90
DOWN=270
LEFT=180
RIGHT=0
SPEED_MOVE = 20
class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.segments = []
        self.paddle(position)
        self.y_position = 0

    def paddle(self,position):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def move_up(self):
        if self.y_position <= 220:
            self.y_position = self.ycor() + SPEED_MOVE
            self.goto(x=self.xcor(),y=self.y_position)

    def move_down(self):
        if self.y_position >= -220:
            self.y_position = self.ycor() - SPEED_MOVE
            self.goto(x=self.xcor(),y=self.y_position)

