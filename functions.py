# functions for actions
import random
import string
import GUI


def generate_password():
    password = ''
    if (GUI.varDigi.get() == 1) & (GUI.varChLower.get() == 1) & (GUI.varChUpper.get() == 1):
        strin = string.ascii_letters
        for i in range(10):
            chornumb = random.choice(['ch', 'digi'])
            if chornumb == 'ch':
                password = password + random.choice(strin)
            else:
                password = password + str(random.randint(0, 10))
    elif (GUI.varDigi.get() == 1) & (GUI.varChLower.get() == 1) & (GUI.varChUpper.get() == 0):
        strin = string.ascii_lowercase
        for i in range(10):
            chornumb = random.choice(['ch', 'digi'])
            if chornumb == 'ch':
                password = password + random.choice(strin)
            else:
                password = password + str(random.randint(0, 10))
    elif (GUI.varDigi.get() == 1) & (GUI.varChLower.get() == 0) & (GUI.varChUpper.get() == 1):
        strin = string.ascii_uppercase
        for i in range(10):
            chornumb = random.choice(['ch', 'digi'])
            if chornumb == 'ch':
                password = password + random.choice(strin)
            else:
                password = password + str(random.randint(0, 10))
    elif (GUI.varDigi.get() == 0) & (GUI.varChLower.get() == 1) & (GUI.varChUpper.get() == 1):
        strin = string.ascii_letters
        for i in range(10):
            password = password + random.choice(strin)
    elif (GUI.varDigi.get() == 0) & (GUI.varChLower.get() == 0) & (GUI.varChUpper.get() == 1):
        strin = string.ascii_uppercase
        for i in range(10):
            password = password + random.choice(strin)
    elif (GUI.varDigi.get() == 0) & (GUI.varChLower.get() == 1) & (GUI.varChUpper.get() == 0):
        strin = string.ascii_lowercase
        for i in range(10):
            password = password + random.choice(strin)
    elif (GUI.varDigi.get() == 1) & (GUI.varChLower.get() == 0) & (GUI.varChUpper.get() == 0):
        for i in range(10):
            password = password + str(random.randint(0, 10))
    else:
        GUI.lblError.config(text='error!')
    # print(password)
    print(str(GUI.varDigi.get()) + ', ' + str(GUI.varChLower.get()) + ', ' + str(GUI.varChUpper.get()))
    # print(strin)
    GUI.lblPassword.config(text=password)


def copy_pass():
    toclpboard = GUI.lblPassword.cget("text")
    GUI.root.clipboard_clear()
    GUI.root.clipboard_append(toclpboard)
