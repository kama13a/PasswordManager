import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password":password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please make sure you haven't left any fields empty.")
    else:
        #TODO 1: If file doesn't exist then create new file and write there
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file, indent=4 )
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH INFORMATION ------------------------------- #

def search():
    website = website_entry.get()
    # TODO 2: the finding web-entry process:
    # open JSON file and use load
    try:
        with open("data.json", "r") as data_file:
            data_dict = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title="Error", message="No Data File Found")
        return
    #use the dict to search for key and get the info from this key

    # TODO 3: When user search the website entry , return:
    if website in data_dict:
        value = data_dict[website]
        # Success: The popup with web-entry title and the info email and password
        messagebox.showinfo(title=website, message=f"Email: {value['email']}\nPassword: {value['password']}")
        # Fail: Popup with error message "No Data File found"
    else:
        messagebox.showerror(title="Error", message=f"No details for {website} exist.")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg="white", pady=50, padx=50)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0, pady=(0, 10), sticky="e", padx=(0, 10))

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0, sticky="e", padx=(0, 10))

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, pady=(0, 10), padx=(0, 10), sticky="e")

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="w")

email_entry = Entry(width=35)
email_entry.insert(0, "angela@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, pady=(10, 10), sticky="w")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w", pady=(10, 10))

# Buttons
generate_password_button = Button(text="Generate Password", bg="white",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=36, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

search_button = Button(text="Search", bg="white", command=search)
search_button.grid(row=1, column=2, padx=(10, 0), sticky="w")

window.mainloop()