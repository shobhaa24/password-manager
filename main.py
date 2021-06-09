from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entry_website.get()
    email_id = entry_email.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_id,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOps", message="Hey! don't leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, 'end')
            password_entry.delete(0, 'end')


def search():
    website_name = entry_website.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            if data[website_name]:
                name = data[website_name]
        except KeyError:
            messagebox.showinfo(title="Oops", message="No website found!")
        else:
            messagebox.showinfo(title="Details", message=f"Email id: {name['email']}\n Password: {name['password']}")


# ---------------------------- UI SETUP ------------------------------- #



windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50, bg="white")


#website labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)


#Entry
entry_website = Entry(width=21)
entry_website.grid(row=1, column=1)
entry_website.focus()
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, string="shobha@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#buttons
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)



windows.mainloop()