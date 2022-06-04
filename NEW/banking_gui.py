import tkinter as Tk

from tkinter import *
import os
from PIL import ImageTk, Image

#MAIN SCREEN
master = Tk()
master.title("Banco Central de ColoTube")


#Functions
def Register():

    #VARIABLES

    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()


    #FUNCTIONS

    def finish_registation():
        print(f"Hey! {temp_name} welcome to the banck of the people")

    
    #Creamos un pop-up window
    register_screen = Toplevel(master)

    register_screen.title("Register")

    #LABELS
    Label(register_screen, text="Please Enter your details below to register", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="Name", font=("Calibri", 12)).grid(row=1, sticky=W)
    Label(register_screen, text="Age", font=("Calibri", 12)).grid(row=2, sticky=W)
    Label(register_screen, text="Gender", font=("Calibri", 12)).grid(row=3, sticky=W)
    Label(register_screen, text="Password", font=("Calibri", 12)).grid(row=4, sticky=W)

    #ENTRIES

                                    #Lo que se agregue en el form queda agregado en la variabe 
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
                                                        #Se le agregó que no se pueda ver la contra
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=4, column=0)


    #Buttons
    Button(register_screen, text="Register", command=finish_registation, font=("Calibri", 12)).grid(row=5, sticky=N, pady=10)



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


