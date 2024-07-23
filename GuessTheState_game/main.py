import turtle
import pandas

screen = turtle.Screen()
text = turtle.Turtle()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
answer_state = (screen.textinput(title="Guess the state", prompt="What's the state name ?")).title()
while answer_state != "exit":

    data = pandas.read_csv("50_states.csv")
    if (data == answer_state).any().any():
        coordinates = data[data["state"] == answer_state]
        x_cor = int(coordinates["x"])
        y_cor = int(coordinates["y"])
        text.penup()
        text.hideturtle()
        text.goto(x_cor, y_cor)
        text.write(f"{answer_state}", align="center", font=("Arial", 10, "normal"))
        answer_state = (screen.textinput(title="Guess the state", prompt="What's the state name?")).title()
    else:
        answer_state = (screen.textinput(title="Guess the state", prompt="Not a state. Guess again !")).title()

turtle.mainloop()
