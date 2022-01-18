from cgitb import text
from curses.ascii import US
from json.tool import main
from tkinter import *
from tkinter import ttk as ttk

## Importacion de la clase usuario
from usuario import User


def createGUI():
    """
    Esta funcion crea una interfaz con Tkinter
    """
    #Ventana principal
    root = Tk()
    root.title("Banco Central de ColoTube")

    #MainFrame

    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=480,height=320,bg="cyan")

    titulo = Label(mainFrame,text="Login de usuario",font=("Arial",24))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

    #Cargar elementos de interfaz

    #Textos y titulos
    nombreLabel = Label(mainFrame,text="Nombre: ")
    nombreLabel.grid(column=0,row=1)

    passwordLabel = Label(mainFrame,text="Contraseña: ")
    passwordLabel.grid(column=0,row=2)

    #Entradas de texto

    nombreUsuario = StringVar()

    nombreEntry = Entry(mainFrame,textvariable=nombreUsuario)
    nombreEntry.grid(column=1,row=1)

    passwordUsuario = StringVar()

    passwordEntry = Entry(mainFrame,textvariable=passwordLabel,show="*")
                                        #Cada caracter lo muestra con *
                                        
    passwordEntry.grid(column=1,row=2)

    # Botones

    LoginButton = ttk.Button(mainFrame,text="Iniciar Sesion",command=iniciarSesion)
                                                    #Con command llamamos la funcion que ejecutara el boton 
    LoginButton.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    RegisterButton = ttk.Button(mainFrame,text="Registar un usuario")
    RegisterButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    root.mainloop()

def iniciarSesion():
    """
    Esta funcion es el evento para el boton iniciar sesion 
    """
    pass

if __name__ == "__main__":

    ## Aqui lo creamos manualmente, pero la gracia seria hacerlo por si solo con el login que definimos 
    user1 = User(input("Ingrese su nombre: ", input("Ingrese su contraseña: ", input("Ingrese su numero de cuenta: "))))

    createGUI()

    


