from tkinter import *
from flashcard import Flashcard

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Chinese Flashcard App")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
flashcard = Flashcard()
card = flashcard.select_card()

# Card Layout
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(400, 100, text="Chino", font=("Courier New", 20))
canvas.create_text(400, 263, text=card["Simplified"], font=("Courier New", 80))

# Buttons layout
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
