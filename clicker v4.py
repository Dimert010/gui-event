import tkinter
space = False

number = 0

def plus(event = None):
    global number, space
    number += 1
    space = True
    color()

def minus(event = None):
    global number, space
    number -= 1
    space = False
    color()

def color(event= None):
    global number
    label.config(text=f"{number:.0f}")
    if number == 0:
        label.config(bg='grey')
    elif number < 0:
        label.config(bg='red')
    else:   
        label.config(bg='green')

def colorChange(event = None):
    window.config(bg="yellow")

def  colorRemove(event = None):
    window.config(bg="grey")
    color()

def divide(event = None):
    global number, space
    if space == True:
        number *= 3
        label.config(text=f"{number:.0f}")
    elif space == False:
        number /= 3
        label.config(text=f"{number:.0f}")
    color()




window = tkinter.Tk()
window.geometry('300x300')

label = tkinter.Label(text=f"{number}", bg= 'brown', fg='white', font=('danger', 20))
label.place(relx=0.5, rely=0.5, anchor='center')


button = tkinter.Button(text='+', bg='green', fg='white', width=20, height=5)
button.configure(command=plus)
button.pack(side=tkinter.TOP)

button1 = tkinter.Button(text='-', bg='red', fg='white', width=20, height=5)
button1.configure(command=minus)
button1.pack(side=tkinter.BOTTOM)

label.bind("<Enter>", colorChange)
label.bind("<Leave>", colorRemove)
label.bind("<Double-Button-1>", divide)
label.bind("<Double-Button-2>", divide)
window.bind("+", plus)
window.bind("-", minus)
window.bind("<space>", divide)

window.mainloop()