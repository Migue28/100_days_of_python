from tkinter import *
from flashcard import Flashcard

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Chinese Flashcard App")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
flashcard = Flashcard(10)
language = "zh"
TIMER = 5000


def show_card():
    global language
    image = PhotoImage()
    card_title = ""
    card_word = ""
    if language == "zh":
        card_title = "Chino"
        card_word = "Simplified"
        image = card_front_image
        pinyin = "Pinyin"
        canvas.itemconfig(canvas_card_pinyin, text=card[f"{pinyin}"])

    elif language == "es":
        card_title = "Español"
        card_word = "G_Meaning"
        image = card_back_image
        canvas.itemconfig(canvas_card_pinyin, text="")
    canvas.itemconfig(canvas_card_image, image=image)
    canvas.itemconfig(canvas_card_title, text=f"{card_title}")
    canvas.itemconfig(canvas_card_word, text=card[f"{card_word}"].capitalize())


def change_language():
    global language
    if language == "zh":
        language = "es"
    elif language == "es":
        language = "zh"


def change_selected_card():
    global card, language
    card = flashcard.select_card()
    language = "zh"
    show_card()
    change_language()
    window.after(TIMER, show_card)


def change_select_and_remove_card():
    global card, language
    flashcard.remove_right_card(card)
    card = flashcard.select_card()
    language = "zh"
    show_card()
    change_language()
    window.after(TIMER, show_card)


# Card Layout
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
canvas_card_image = canvas.create_image(400, 263)
canvas.grid(row=0, column=0, columnspan=2)


# Buttons layout
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

# Card behavior
card = flashcard.select_card()
canvas_card_title = canvas.create_text(400, 100, font=("Courier New", 20))
canvas_card_pinyin = canvas.create_text(400, 150, font=("Courier New", 20))
canvas_card_word = canvas.create_text(400, 263, font=("Courier New", 80))

# Button behavior
wrong_button.config(command=change_selected_card)
right_button.config(command=change_select_and_remove_card)

# App behavior
show_card()
change_language()
window.after(TIMER, show_card)

window.mainloop()
