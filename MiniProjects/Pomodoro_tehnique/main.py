from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        counter(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        counter(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        counter(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, counter, int(count) - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label["text"] = marks


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
# timer_label.pack(side="top")
timer_label.grid(column=1, row=0)

# Create center image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # convert image to tkinter photo img
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

# Create the buttons
button_start = Button(height=2, width=5, text="Start", font=(FONT_NAME, 10), justify=CENTER, background="white",
                      command=start_timer)
# button_start.pack(side="left")
button_start.grid(column=0, row=2)
button_stop = Button(height=2, width=5, text="Reset", font=(FONT_NAME, 10), justify=CENTER, background="white",
                     command=reset_timer)
# button_stop.pack(side="right")
button_stop.grid(column=2, row=2)

checkmark_label = Label(font=(FONT_NAME, 30), pady=50, bg=YELLOW, fg=GREEN)
# checkmark_label.pack(side="bottom")
checkmark_label.grid(column=1, row=3)
window.mainloop()
