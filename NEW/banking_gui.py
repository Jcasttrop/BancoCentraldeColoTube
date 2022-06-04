import tkinter as Tk

from tkinter import *
import os
from PIL import ImageTk, Image

#MAIN SCREEN
master = Tk()
master.title("Banco Central de ColoTube")


#Functions
def Register():
    
    #Creamos un pop-up window
    register_screen = Toplevel(master)

    register_screen.title("Register")

    #LABELS
    Label(register_screen, text="Please Enter your details below to register", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)


def Login():
    pass



#IMAGE IMPORT
img = Image.open("BCT1.jpg")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)


#Labels
Label(master, text="Banco Cetral de ColoTube", font=("Calibri",14)).grid(row=0, sticky=N, pady=10)
Label(master, text="El banco de la gente", font=("Calibri",10)).grid(row=1, sticky=N)

Label(master, image=img).grid(row=2, sticky=N, pady=16)


#Buttons
Button(master, text="Register", font=("Calibri", 12),width=20, command=Register).grid(row=3,sticky=N)
Button(master, text="Login", font=("Calibri", 12),width=20, command=Login).grid(row=4,sticky=N, pady=10)


master.mainloop()


