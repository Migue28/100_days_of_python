from tkinter import *

window = Tk()
window.title("My GUI with Tkinter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    my_label.config(text=f"{user_input.get()}")


my_label = Label(text="This a label I created.", font=("Arial", 24))
my_label.grid(row=0, column=0)

button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="Click me too", command=button_clicked)
new_button.grid(row=0, column=2)

user_input = Entry(width=10)
user_input.grid(row=3, column=3)

window.mainloop()
