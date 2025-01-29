from tkinter import *
from random import randint

root = Tk()
root.title("Are You Dumb")
root.geometry("600x400")
root.config(bg="black")

def yes():
    yes_button.pack_forget()
    no_button.pack_forget()
    dumb_label.configure(text="I Knew It")

def no():
    random_int_x = randint(0, 600)
    random_int_y = randint(0, 400)
    no_button.place(x=random_int_x, y=random_int_y)

dumb_label = Label(root, text="Are You Dumb", font=("Arial", 30), bg="black", fg="white")
dumb_label.pack(pady=7, padx=7)

yes_button = Button(root, text="Yes", font=("Arial", 17), command=yes, bg="black", fg="white")
yes_button.pack(pady=7)
yes_button.place(x=200, y=100)

no_button = Button(root, text="No", font=('Arial', 17), command=no, bg="black", fg="white")
no_button.pack(pady=7)
no_button.place(x=300, y=100)

root.mainloop()
