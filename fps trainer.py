import tkinter as tk
from tkinter import *
import random

score = 0
timer = 20

lst = ["w", "a", "s", "d", "<space>", "<button-1>", "<Double-Button-1>", "<Triple-Button-1>"]

def start(event = None):
    countdown()
    randomBut()

def countdown(event = None):
    global timer
    if timer > 0:
        button.destroy()
        timer -=1
        window.after(1000, countdown)
        timer_label.config(text=f"time remaining: {timer}")

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()
    for i in lst:
        window.unbind(i)
    randomBut()

def randomBut(event = None):
    global score
    item = random.choice(lst)
    if timer > 0:
        label4 = tk.Label(frame, text=item, bg= "orange", fg= "white",font = ("danger", 15))
        label4.place(x=random.randint(50, 450), y=random.randint(50, 450))
        if item == "w":
            window.bind("<w>", lambda event: clear_frame())
            score += 2
            score_bijhouden_label.config(text=f"score: {score}")
        elif item == "a":
            window.bind("<a>", lambda event: clear_frame())
            score += 2
            score_bijhouden_label.config(text=f"score: {score}")
        elif item == "s":
            window.bind("<s>", lambda event: clear_frame())
            score += 2
            score_bijhouden_label.config(text=f"score: {score}")
        elif item == "d":
            window.bind("<d>", lambda event: clear_frame())
            score += 2
            score_bijhouden_label.config(text=f"score: {score}")
        elif item == "<space>":
            window.bind("<space>", lambda event: clear_frame())
            score += 2
            score_bijhouden_label.config(text=f"score: {score}")
        elif item == "<button-1>":
            label4.bind("<Button-1>", lambda event: clear_frame())
            score += 1
            score_bijhouden_label.config(text=f"score: {score}")
        elif item == "<Double-Button-1>":
            label4.bind("<Double-Button-1>", lambda event: clear_frame())
            score += 1
            score_bijhouden_label.config(text=f"score: {score}")
        elif item == "<Triple-Button-1>":
            label4.bind("<Triple-Button-1>", lambda event: clear_frame())
            score += 1
            score_bijhouden_label.config(text=f"score: {score}")       

window = tk.Tk()
window.geometry('500x500')	
window.title('FPS Trainer')

frame = Frame(window)
frame.pack(side="top", fill="both", expand=True)
timer_label = tk.Label(text=f"time remaining: {timer}", bg= 'brown', fg='white', font=('danger', 20), width=30, height=1)
timer_label.pack()

score_bijhouden_label = tk.Label(text=f"score: {score}", bg= 'brown', fg='white', font=('danger', 20), width=30, height=1)
score_bijhouden_label.pack()

button = tk.Button(text='click here', bg='green', fg='white', width=20, height=5, command=start)
button.place(relx=0.5, rely=0.5, anchor='center')
button.bind('<Button-1>', start)

window.mainloop()