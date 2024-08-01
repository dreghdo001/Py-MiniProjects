from tkinter import *
import pandas
import random

FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"

# Getting data
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/data.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    """Change the card after 3 seconds"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="Romanian", fill="black")
    canvas.itemconfig(word_text, text=current_card["Romanian"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flip the background image and text"""
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def is_known():
    """Remove the known word and create a new csv files with the words remaining"""
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Create window
window = Tk()
window.title("Translator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create the canvas from center
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
language_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "bold", "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))

# Create buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

# Next the card function
next_card()


