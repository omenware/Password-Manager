from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
GRAY="E7E0C9"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters= [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list=password_numbers+password_symbols+password_letters
    random.shuffle(password_list)
    password = "".join(password_list)
    password_box.insert(0, f'{password}')
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website_input=website_box.get()
    email_input=email_box.get()
    password_input=password_box.get()
    new_data={
        website_input: {
            'Email': email_input,
            'password': password_input

         }

    }

    if len(email_input)==0 or len(password_input)==0:
        messagebox.showerror(title='Oops', message="Please check you have fill the every entry.")
    else:
         # is_ok=messagebox.askokcancel(title='Imortant Message', message=f'These are the details entered: \n Email: {email_input}\nPassword: {password_input}\n Is it ok to save?')
         # if is_ok:
            try:
                with open('data.json', mode='r') as data:
                    data_file=json.load(data)
            except FileNotFoundError:
                with open("data.json", mode='w') as data:
                    json.dump(new_data, data, indent=4)
            else:
                data_file.update(new_data)
                with open('data.json', mode='w') as data:
                    json.dump(data_file, data , indent=4)
            finally:
                website_box.delete(0,END)
                password_box.delete(0,END)
# ---------------------------- SEARCH------------------------------- #

def search():
    website_input=website_box.get()
    try:
        with open('data.json') as data:
            report = json.load(data)
    except FileNotFoundError:
        messagebox.showerror(title='Oops', message='File does not exist.' )
    else:
        if website_input in report:
            email=report[website_input]['Email']
            password=report[website_input]['password']
            messagebox.showinfo(title='website', message=f'Email: {email}\npassword: {password}')



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pasword Manager')
# window.minsize(width=300,height=400)
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
lock_img=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

# ---------------------------- LABELS ------------------------------- #
website_label=Label(text='Website:')
website_label.grid(row=1,column=0)

email_label=Label(text='Email/Username:')
email_label.grid(row=2,column=0)

password_label=Label(text='Password:')
password_label.grid(row=3,column=0)

# ---------------------------- BUTTONS ------------------------------- #
generate_button=Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text='Add',width=36,command=add)
add_button.grid(row=4, column=1, columnspan=2)

search_button=Button(text='Search',width=14, bg='red',command=search)
search_button.grid(row=1, column=2)

# ---------------------------- ENTRIES ------------------------------- #
website_box=Entry(width=21)
website_box.focus()
website_box.grid(row=1,column=1)

email_box=Entry(width=35)
email_box.grid(row=2,column=1,columnspan=2)
email_box.insert(0,'73prisingh@gmail.com')

password_box=Entry(width=21)
password_box.grid(row=3,column=1)
window.mainloop()