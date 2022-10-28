from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_app():
    global repetitions
    global timer
    window.after_cancel(timer)
    repetitions = 0
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetitions
    repetitions += 1
    # 25 minutes lapses
    # 1 min = 60 secs
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN
    if repetitions % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Working", fg=GREEN)
    elif repetitions % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
        check_text = check_label.cget("text")
        check_text += "✓"
        check_label.config(text=check_text)
    elif repetitions % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
        check_text = check_label.cget("text")
        check_text += "✓"
        check_label.config(text=check_text)
    else:
        count_down(work_sec)
        title_label.config(text="Working", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"),
                    bg=YELLOW, highlightthickness=0, fg=GREEN)
title_label.grid(row=0, column=1)

check_label = Label(text="", font=(FONT_NAME, 20, "bold"),
                    bg=YELLOW, highlightthickness=0, fg=GREEN)
check_label.grid(row=3, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 15), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 15), command=reset_app)
reset_button.grid(row=2, column=2)

window.mainloop()
