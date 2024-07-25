from turtle import Turtle, Screen

timmy = Turtle()



def move_forward():
    timmy.forward(50)
def move_backwords():
    timmy.forward(-50)

def turn_right():
    new_heading = timmy.heading() - 30
    timmy.setheading(new_heading)

def turn_left():
    new_heading = timmy.heading() + 30
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwords)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()