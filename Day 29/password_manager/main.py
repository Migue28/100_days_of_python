from tkinter import *
from tkinter import messagebox

WHITE = "#ffffff"


# TODO 2: Generate random password
def generate_password():
    pw = ""


# TODO 3: Clip generated password in clipboard to paste easily
# TODO 4: Save generated tuple to a file
def save_account():
    web_name = user_web.get()
    user_name = user_mail.get()
    password_name = password.get()
    account_format = f"Web: {web_name} || User: {user_name} || Password: {password_name}\n"
    if messagebox.askokcancel(message=f"Want to save this account? User: {user_name}, password: {password_name}"):
        print("Esto entro")
        if web_name != "" and user_name != "" and password_name != "":
            with open(mode="a", file="saved_accounts.txt") as file:
                file.write(account_format)
            user_web.delete(0, END)
            password.delete(0, END)
        else:
            messagebox.showerror(title="Oh oh", message="All fields are necessary")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=190, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo_image)
canvas.grid(row=0, column=1)

# TODO 1: Request website name, user/email and password from user
user_web_label = Label(text="Website:")
user_web_label.grid(row=1, column=0)

user_web = Entry(width=51)
user_web.insert(END, "")
user_web.grid(row=1, column=1, columnspan=2)
user_web.focus()

user_mail_label = Label(text="Email/Username:")
user_mail_label.grid(row=2, column=0)

user_mail = Entry(width=51)
user_mail.insert(END, "example@mail")
user_mail.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password = Entry(width=32)
password.insert(END, "")
password.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_password_button = Button(text="Save", width=43, command=save_account)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
