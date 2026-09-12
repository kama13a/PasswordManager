import os
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password_generated = "".join(password_list)
    password_entry.insert(0, password_generated)

    pyperclip.copy(password_generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #

#TODO 2: get all the info and save in the .csv file
    # create the fn for the button save
    # check if user inserted all the info
        # Yes: save the info and use data frame
        # No: ask the user to insert all the info
CSV_file = "passwords.csv"
def load_records():
    if os.path.exists(CSV_file):
        return pd.read_csv(CSV_file).to_dict(orient="records")
    return []
import os
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password_generated = "".join(password_list)
    password_entry.insert(0, password_generated)

    pyperclip.copy(password_generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #

#TODO 2: get all the info and save in the .csv file
    # create the fn for the button save
    # check if user inserted all the info
        # Yes: save the info and use data frame
        # No: ask the user to insert all the info
CSV_file = "passwords.csv"
def load_records():
    if os.path.exists(CSV_file):
        return pd.read_csv(CSV_file).to_dict(orient="records")
    return []

records = load_records()

def save():
    website = web_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    # Every time you press the button:
        # Save the website to the web_list
        # Save the email to the email_list
        # Save the password to the password_list
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: "
                                                              f"{email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            records.append({
                "website" : website,
                "email" : email,
                "password" : password
            })

            df = pd.DataFrame(records)
            df.to_csv(CSV_file, index=False)
            print(df)
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window_s = Tk()
window_s.title("Password Manager")
window_s.config(
                bg="white",pady=50, padx=50)

# TODO 1: Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

web_label = Label()
web_label.config(text="Website:", bg="white" )
web_label.grid(row=1, column=0, pady=(0, 10), sticky="e", padx=(0, 10))

web_entry = Entry()
web_entry.focus()
web_entry.config(width=35)
web_data = web_entry.get()
web_entry.grid(row=1, column=1, columnspan=2, pady=(0, 10), sticky="w")

user_label = Label()
user_label.config(text="Email/Username:", bg="white")
user_label.grid(row=2, column=0, sticky="e", padx=(0, 10))

user_entry = Entry()
user_entry.config(width=35)
user_entry.insert(END, "angela@email.com")
user_entry.grid(row=2, column=1, columnspan=2, pady=(0, 10), sticky="w")

password_label = Label()
password_label.config(text="Password:", bg="white")
password_label.grid(row=3, column=0, pady=(0, 10), sticky="e", padx=(0, 10))

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(row=3, column=1, pady=(0, 10), sticky="w")

p_button = Button()
p_button.config(text="Generate Password", bg="white", command=generate_password)
p_button.grid(row=3, column=2, pady=(0, 10  ), sticky="w")

add_button = Button()
add_button.config(text="Add", width=36, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window_s.mainloop()
records = load_records()

def save():
    website = web_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    # Every time you press the button:
        # Save the website to the web_list
        # Save the email to the email_list
        # Save the password to the password_list
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: "
                                                              f"{email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            records.append({
                "website" : website,
                "email" : email,
                "password" : password
            })

            df = pd.DataFrame(records)
            df.to_csv(CSV_file, index=False)
            print(df)
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window_s = Tk()
window_s.title("Password Manager")
window_s.config(
                bg="white",pady=50, padx=50)

# TODO 1: Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

web_label = Label()
web_label.config(text="Website:", bg="white" )
web_label.grid(row=1, column=0, pady=(0, 10), sticky="e", padx=(0, 10))

web_entry = Entry()
web_entry.focus()
web_entry.config(width=35)
web_data = web_entry.get()
web_entry.grid(row=1, column=1, columnspan=2, pady=(0, 10), sticky="w")

user_label = Label()
user_label.config(text="Email/Username:", bg="white")
user_label.grid(row=2, column=0, sticky="e", padx=(0, 10))

user_entry = Entry()
user_entry.config(width=35)
user_entry.insert(END, "angela@email.com")
user_entry.grid(row=2, column=1, columnspan=2, pady=(0, 10), sticky="w")

password_label = Label()
password_label.config(text="Password:", bg="white")
password_label.grid(row=3, column=0, pady=(0, 10), sticky="e", padx=(0, 10))

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(row=3, column=1, pady=(0, 10), sticky="w")

p_button = Button()
p_button.config(text="Generate Password", bg="white", command=generate_password)
p_button.grid(row=3, column=2, pady=(0, 10  ), sticky="w")

add_button = Button()
add_button.config(text="Add", width=36, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window_s.mainloop()