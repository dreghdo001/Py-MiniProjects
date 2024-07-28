from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from password_generator import password_generator


def new_pass():
    new_password = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showerror(title="oops", message="Please fill all the entry's")
    else:
        message = messagebox.askokcancel(title=website,
                                         message=f"Details: \nEmail/Username: {username}\nPassword: {password}\n"
                                                 f"Do you want to save ? ")
        if message:
            data_entry = f"{website} | {username} | {password}\n"
            with open("data.txt", mode="a") as data:
                data.write(data_entry)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Create canvas image
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
username_label = Label(text="Email/Username: ")
password_label = Label(text="Password: ")

# Text entry
website_entry = Entry(width=50)
username_entry = Entry(width=50)
password_entry = Entry(width=32)

# Positioning
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2)
username_label.grid(column=0, row=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)

# Buttons
button_generate = Button(text="Generate Password", width=14, command=new_pass)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", width=43, command=save_data)
button_add.grid(column=1, row=4, columnspan=2)

website_entry.focus()  # Start the cursor on this entry
username_entry.insert(0, string="dreionut98@gmail.com")

window.mainloop()
