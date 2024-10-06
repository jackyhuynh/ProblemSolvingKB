# https://docs.python.org/3/library/tkinter.html#the-packer
import tkinter
import turtle


# Unlimited positional arguments, unlimited number of inputs
def add(*args):
    sum_ = 0
    for n in args:
        sum_ += n
    return sum_


def calculate(**kwargs):
    print(kwargs)


# Use the tkinter model
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label Create
my_label = tkinter.Label(text='I Am a Label', font=("April", 24))
# Step 2: Lay out on the screen before show up. Use pack
my_label.pack()

tim = turtle.Turtle()
tim.write("My name is Truc Huynh")

# Keep the window on screen
window.mainloop()
