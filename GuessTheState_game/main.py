import turtle
import pandas

screen = turtle.Screen()
text = turtle.Turtle()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv") # reads the data from CSV
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 correct", prompt="What's the state name?")).title()
    if answer_state == "Exit":
        break
    if (data == answer_state).any().any():
        guessed_states.append(answer_state)
        state_data = data[data["state"] == answer_state] # takes the row which correspond with the state entered
        text.penup()
        text.hideturtle()
        text.goto(state_data.x.item(), state_data.y.item()) # takes items/columns x and y from that state
        text.write(f"{answer_state}", align="center", font=("Arial", 10, "normal"))

states_to_learn = []
for el in all_states:
    if el not in guessed_states:
        states_to_learn.append(el)

to_learn_dict = {
    "State": states_to_learn
}
pandas.DataFrame(to_learn_dict).to_csv("states_to_learn.csv")
# turtle.mainloop() keeps the screen opened
