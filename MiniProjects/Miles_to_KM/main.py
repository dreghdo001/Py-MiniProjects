from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=150, height=200)


entry = Entry(width=10)
entry.grid(column=1,row=1)




button = Button(text="Click Me", background="green")
new_button = Button(text="Noob", background="orange")


window.mainloop()