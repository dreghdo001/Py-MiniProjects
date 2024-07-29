from tkinter import *
from tkinter import messagebox
import json
import subprocess
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
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if website == "" or password == "":
        messagebox.showerror(title="oops", message="Please fill all the entry's")
    else:
        message = messagebox.askokcancel(title=website,
                                         message=f"Details: \nEmail/Username: {username}\nPassword: {password}\n"
                                                 f"Do you want to save ? ")
        if message:
            try:
                with open("data.json", mode="r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", mode="w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                # Empty the entryes
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


def search_data():
    user_search = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if user_search == "":
            messagebox.showinfo(title="Error", message=f"Enter the account you're looking for !")
        elif user_search in data:
            messagebox.showinfo(title=f"{user_search}",
                                message=f"Username: {data[user_search]['username']}\n"
                                        f"Password: {data[user_search]['password']}\n"
                                        f"Password copied in the clipboard !\n")
            # Copy password in the clipboard !
            window.clipboard_append(data[user_search]['password'])
            password_entry.delete(0, END)
            password_entry.insert(0, data[user_search]['password'])
        else:
            messagebox.showinfo(title="Error", message=f"{user_search} account not registered !")


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
website_label = Label(text="Website: ", pady=2)
username_label = Label(text="Email/Username: ", pady=2)
password_label = Label(text="Password: ", pady=2)

# Text entry
website_entry = Entry(width=32)
username_entry = Entry(width=50)
password_entry = Entry(width=32)

# Positioning
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1)
username_label.grid(column=0, row=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)

# Buttons
button_generate = Button(text="Generate Password", width=14, command=new_pass)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=43, command=save_data)
button_add.grid(column=1, row=4, columnspan=2)

button_search = Button(text="Search", width=14, command=search_data)
button_search.grid(column=2, row=1)

website_entry.focus()  # Start the cursor on this entry
username_entry.insert(0, string="dreionut98@gmail.com")

window.mainloop()
