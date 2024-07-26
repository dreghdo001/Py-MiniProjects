from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=150)
window.config(padx=5,pady=5)

entry = Entry(width=10, font=15, fg="black", justify = "center")
# entry.place(relx=.5, rely=.3, anchor=CENTER)
entry.grid(column=1, row=0)

miles_text_label = Label(text=" miles ", font=15)
# miles_text.place(relx=.7, rely=.3, anchor=CENTER)
miles_text_label.grid(column=2, row=0)

km_text_label = Label(text=" km ", font=15)
# km_text.place(relx=.7, rely=.5, anchor=CENTER)
km_text_label.grid(column=2, row=1)

message_label = Label(text="is equal to", font=15)
# message.place(relx=0.2, rely=.5, anchor=CENTER)
message_label.grid(column=0, row=1)

result_label = Label(text="", font=18)
# result.place(relx=.5, rely=.5, anchor=CENTER)
result_label.grid(column=1, row=1)

def calculator():
    result_label["text"] = round(float(entry.get()) * 1.609347, 2)

button = Button(text="Calculate", background="gray", width=10, command=calculator)
# button.place(relx=.5, rely=.7, anchor=CENTER)
button.grid(column=1,row=2)
window.mainloop()
