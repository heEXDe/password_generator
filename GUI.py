# GUI for the program
from tkinter import *
import functions

root = Tk()
root.title('password generator v 1.0')
root.resizable(0, 0)

var = IntVar()
varDigi = IntVar()
varChLower = IntVar()
varChUpper = IntVar()

lblPassword = Label(root, text='....................')
lblPassword.grid(row=0, column=1, padx=10, pady=15)
btnGenerate = Button(root, text='Generate', command=lambda: functions.generate_password())
btnGenerate.grid(row=1, column=0, padx=10)
btnCopy = Button(root, text='Copy', command=lambda: functions.copy_pass())
btnCopy.grid(row=1, column=2, padx=10)
chDigits = Checkbutton(root, text='Digits', variable=varDigi, onvalue=1, offvalue=0)
chDigits.grid(row=2, column=0, padx=10, pady=7)
chChLower = Checkbutton(root, text='Lower-case', variable=varChLower, onvalue=1, offvalue=0)
chChLower.grid(row=2, column=1, padx=10, pady=7)
chChUpper = Checkbutton(root, text='Upper-case', variable=varChUpper, onvalue=1, offvalue=0)
chChUpper.grid(row=2, column=2, padx=10, pady=7)
lblPassLength = Label(root, text='Password length: ')
lblPassLength.grid(row=3, column=0, padx=10)
scl01 = Scale(root, variable=var, orient=HORIZONTAL, from_=1, to=20)
scl01.grid(row=3, column=1, columnspan=2)
lblError = Label(root, text='')
lblError.grid(row=4, column=1, pady=7)


def gui_start():
    root.mainloop()
