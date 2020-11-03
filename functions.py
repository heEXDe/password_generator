# functions for actions
import random
import string
import GUI


def generate_password(chsm, chbig, digit):
    strin = string.ascii_letters
    password = ''
    if chsm == 1 & chbig == 1 & digit == 1:
        for i in range(10):
            chornumb = random.choice(['ch', 'digi'])
            if chornumb == 'ch':
                password = password + random.choice(strin)
            else:
                password = password + str(random.randint(0, 10))
    # print(password)
    GUI.lblPassword.config(text=password)


def copy_pass():
    toclpboard = GUI.lblPassword.cget("text")
    GUI.root.clipboard_clear()
    GUI.root.clipboard_append(toclpboard)
