from tkinter import *

window = Tk()

def change_color():
    f = open(r'button_state.txt', 'r')
    for line in f.readlines():
        if 'button_notes' in line:
            pass
b = Button(text='Click me', command=lambda: change_color())
b.pack()


window.mainloop()

"""
# Change state
if (button) in line:
    if (WHITE) in line:
        button = YELLOW
        button.config(bg=YELLOW)
    elif (YELLOW) in line:
        button = GREEN
        button.config(bg=GREEN)
    elif (GREEN) in line:
        button = WHITE
        button.config(bg=WHITE)
        
# save state


"""


