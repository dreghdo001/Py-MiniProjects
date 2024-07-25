from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20,pady=200)
# Labels
label = Label(text="New Text", font=24)

#label.pack()

def action():
    label["text"] = f"Hello {entry.get()}"

button = Button(text="Click Me", background="green", command=action)
new_button = Button(text="Noob", background="orange", command=action)

entry = Entry(width=30)
entry.insert(END, string="Enter your name")
print(entry.get())
# Using place
# entry.place(x=0,y=50)
# label.place(x=0,y=0)

# Using grid
label.grid(column=0, row=0)
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
entry.grid(column=3, row=2)

window.mainloop()
