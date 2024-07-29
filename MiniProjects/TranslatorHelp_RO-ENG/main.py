from tkinter import *
from tkinter import messagebox
import pandas
import random

def random_word():
    data = pandas.read_csv("data/data.csv")
    # data_dict = pandas.DataFrame.to_dict(data)
    random_index = random.randint(1, 100)
    romanian_words = data["Romanian"].to_list()
    english_words = data["English"].to_list()
    canvas.itemconfig(language_text, text="Romanian")
    canvas.itemconfig(word_text, text=romanian_words[random_index])


FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Translator")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")

canvas.create_image(400, 263,image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

language_text = canvas.create_text(400,150, text="Title",font=(FONT_NAME, 40, "bold", "italic"))
word_text = canvas.create_text(400,263, text="Word",font=(FONT_NAME, 60, "bold"))

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")




right_button = Button(image=right_image, highlightthickness=0,command=random_word)
wrong_button = Button(image=wrong_image, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)















window.mainloop()