from tkinter import *

FONT = ("Arial", 10, "bold")


def calculate():
    if miles_label.cget("text") == "Miles":
        result = f"{round(float(user_input.get()) * 1.609344, 2)}"
        result_label.config(text=result)
    else:
        result = f"{round(float(user_input.get()) / 1.609344, 2)}"
        result_label.config(text=result)


def invert_units():
    label_1 = miles_label.cget("text")
    label_2 = km_label.cget("text")
    miles_label.config(text=label_2)
    km_label.config(text=label_1)


window = Tk()
window.title("Distance converter")
window.minsize(width=300, height=100)
window.config(padx=5, pady=5)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)
km_label = Label(text="Kilometers", font=FONT)
km_label.grid(row=1, column=2)
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(row=1, column=0)

user_input = Entry(width=10)
user_input.focus()
user_input.grid(row=0, column=1)
result_label = Label(text="0", font=FONT)
result_label.grid(row=1, column=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

invert_unit_button = Button(text="Invert", command=invert_units)
invert_unit_button.grid(row=0, column=3)

window.mainloop()
