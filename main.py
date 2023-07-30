from tkinter import *
from tkinter import messagebox
from random import choice, randint, choice, shuffle
import pyperclip
import json

YELLOW = "#f7f5dd"
RED = "#e7305b"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def find_password():
    try:
        with open("data.json", "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")

    else:
        name = website_Entry.get().title()
        if name in content:
            email = content[name]["email"]
            password = content[name]["password"]
            messagebox.showinfo(f"{name}", f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo("Error", "No Details for the website exists")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    random_password = "".join(password_list)
    Password_Entry.insert(0, random_password)
    pyperclip.copy(random_password)
    messagebox.showinfo("Message", "Your password has been copied to your clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_name = website_Entry.get()
    email_user = Email_Entry.get()
    password = Password_Entry.get()
    new_data = {
        website_name: {
            "email": email_user,
            "password": password,
        }
    }

    if len(website_name) == 0 or len(email_user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!!")

    else:
        try:
            with open("data.json", "r") as file1:
                #Reading the old data
                content = json.load(file1)
        except FileNotFoundError:
            with open("data.json", "w") as file1:
                json.dump(new_data, file1, indent=4)

        else:
            #Updating old data with new data
            content.update(new_data)

            with open("data.json", "w") as file1:
                #Saving updated data
                json.dump(content, file1, indent=4)
        finally:
            website_Entry.delete(0, END)
            Email_Entry.delete(0, END)
            Password_Entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(height=200, width=200, bg=YELLOW, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)  # x,y positon of image and image
canvas.grid(row=0, column=1)

# Labels
website_Label = Label(text="Website:", bg=YELLOW, highlightthickness=0)
website_Label.grid(row=1, column=0)
Email_Label = Label(text="Email:", bg=YELLOW, highlightthickness=0)
Email_Label.grid(row=2, column=0, pady=(20, 0))
Password_Label = Label(text="Password:", bg=YELLOW, highlightthickness=0)
Password_Label.grid(row=3, column=0, pady=(20, 0))

# Entries
website_Entry = Entry(width=25)
website_Entry.grid(row=1, column=1, padx=(22, 0))
website_Entry.focus()
Email_Entry = Entry(width=40)
Email_Entry.grid(row=2, column=1, columnspan=2, pady=(20, 0))
Password_Entry = Entry(width=25)
Password_Entry.grid(row=3, column=1, padx=(22, 0), pady=(20, 0))

# Buttons
Generate_Button = Button(text="Generate Password", command=generate_password, fg=RED)
Generate_Button.grid(row=3, column=2, pady=(20, 0))
Add_Button = Button(text="Add", width=36, command=save)
Add_Button.grid(row=4, column=1, columnspan=2, pady=(20, 0))
Search_Button = Button(text="Search", command=find_password, width=15, fg=RED)
Search_Button.grid(row=1, column=2)
window.mainloop()
