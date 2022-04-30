from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #[new_item for item in list] for list comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #   password += char
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
                    "email": email,
                    "password": password,
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill out all the information")
    else:
        # is_ok = messagebox.askokcancel(title = website, message=f"These are the details entered: \nEmail: {email} "
        #                                                 f"\nPassword: {password} \nis it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                    # data_file.write(f"{website} | {email} | {password}\n")
                    #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file, indent = 4)
        else:
                    #updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                        #saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0, END)
                    # email_entry.delete(0, END)

# ---------------------------- FIND PW  ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width = 200, height = 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan = 2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan = 2)
email_entry.insert(END, "Regal@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan = 2)

#buttons
generate_pw_button = Button(text="Generate Password", width = 30, command=generate_password)
generate_pw_button.grid(column=1, row=4)
search_button = Button(text="Search", width = 30,command = find_password)
search_button.grid(column=1, row=5)
add_button = Button(text="Add", width = 30, command=save)
add_button.grid(column=1, row=6, columnspan = 2)



window.mainloop()