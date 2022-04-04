import tkinter

number = 0

def plus():
    global number
    number += 1
    color()

def minus():
    global number
    number -= 1
    color()

def color(event= None):
    global number
    label.configure(text=number)
    if number == 0:
        label.configure(bg='green')
    elif number < 0:
        label.configure(bg='red')
    else:
        label.configure(bg='blue')

def colorChange(event = None):
    window.config(bg="yellow")

def  colorRemove(event = None):
    window.config(bg="grey")
    color()

def multiply(event = None):
    global number
    number *= 3
    color() 

def divide(event = None):
    global number
    number /= 3
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
label.bind("<Double-Button-1>", multiply)
label.bind("<Double-Button-2>", divide)

window.mainloop()