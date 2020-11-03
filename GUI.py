# GUI for the program
from tkinter import *
import functions

root = Tk()
root.title('password generator v 1.0')
root.resizable(0, 0)

lblPassword = Label(root, text='....................')
lblPassword.grid(row=0, column=0, padx=50, pady=50)
btnGenerate = Button(root, text='Generate', command=lambda: functions.generate_password(1, 1, 1))
btnGenerate.grid(row=0, column=1)
btnCopy = Button(root, text='Copy', command=lambda: functions.copy_pass())
btnCopy.grid(row=0, column=2, padx=10)


def gui_start():
    root.mainloop()
