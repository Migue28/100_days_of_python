from tkinter import *

WHITE = "#ffffff"
# TODO 1: Accept website name, user/email and password from user
# TODO 2: Generate random password
# TODO 3: Clip generated password in clipboard to paste easily
# TODO 4: Save generated account to a file

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=190, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo_image)
canvas.grid(row=0, column=1)

# TODO 1: Request website name, user/email and password from user
user_web_label = Label(text="Website: ", padx=10)
user_web_label.grid(row=2, column=0)

user_web = Entry(width=50)
user_web.insert(END, "")
user_web.grid(row=2, column=1)
user_web.focus()

user_mail_label = Label(text="Email/Username: ", padx=10)
user_mail_label.grid(row=3, column=0)

user_mail = Entry(width=50)
user_mail.insert(END, "")
user_mail.grid(row=3, column=1)

password_label = Label(text="Password: ", padx=10)
password_label.grid(row=4, column=0)

password = Entry(width=20)
password.insert(END, "")
password.grid(row=4, column=1)

generate_password_button = Button(text="Generate password")
generate_password_button.grid(row=4, column=2)

add_password_button = Button(text="Add", width=50)
add_password_button.grid(row=5, column=1)

window.mainloop()
