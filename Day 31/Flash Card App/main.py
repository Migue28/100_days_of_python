from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Chinese Flash Card App")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Card Layout
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_back_image)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons layout
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
