import time
from tkinter import *
from time import strftime
import tkinter  as tk 

clock = tk.Tk()
clock.geometry("500x500")
clock.resizable(0,0)
clock.title('Horloge')


def show():
    print("ok")

def set():
    print("reglage")


button0 = Button( clock , text = "set" ,bg = 'blue', fg= 'white', command = set )
button0.place(x=100, y=400)

button1 = Button( clock , text = "alarm" , bg = 'red',fg= 'white', command = show )
button1.place(x=400, y=400)


def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)

mark = Label(clock,
            font = ('calibri', 40, 'bold'),
            pady=100,
            foreground = 'black',
            background= 'ivory')

mark.pack(anchor = 'center')
time()





clock.mainloop()
