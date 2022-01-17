import random

def AccountNumberGenerator() -> int:
    """
    Esta funcion genera un numero de cuenta unico a cada usuario

    Esto lo hace comprobando que cada numero de cuenta sea distinto para cada usuario 
    """

    possibleNumbers = [1,2,3,4,5,6,7,8,9,0]

    listForAccoun = []

    for i in range(9):
        union = random.choice(possibleNumbers)
        listForAccoun.append(union)

    numberAccount = "".join(listForAccoun)

    return numberAccount


def generatepassword() -> int:
    """
    Esta funcion genera un a contraseña de 15 caracteres al usuario.

    La funcion no necesita de ningun argumento 
    """

    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
            '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = MAYUS + MINUS + NUMS + CHARS

    password = []

    for i in range(15):
        elegidos = random.choice(caracteres)
        password.append(elegidos)

    contra = "".join(password)   #convertimos la lista en un str
    
    return password
class User():
    pass

    def __init__(self,name,password,account_number):
        self.name = name
        self.password = password
        self.account_number = account_number

        self.isRegistered = False

    def registrarUsuario(self):
        print("Hey! Bienvenido al Banco de ColoTube, vamos a registarte")
        name = input("Por favor ingrese su nombre: ")

        #Genera la contraseña al usuario
        password = generatepassword()
        print(f"Por favor recuerda esta contraseña segura: {password}")

        #Le pregunta al usuario que si quiere cambiar la contraseña
        print("La contraseña que te dimos cumple con altos estandares de seguridad")

        eleccionCambioContraseña = input("¿Deseas personalizar tu contraseña?" )
        eleccionCambioContraseñaCONSOLA = eleccionCambioContraseña.lower()

        if eleccionCambioContraseñaCONSOLA == "si":
            newPassword = input("Tu nueva contraseña debe tener al menos 9 caracteres\nIngresa tu nuva contraseña: ")
            # Evalua la condicion
            if len(password) >= 9:
                newPassword = password
            else:
                pass

        account_number = AccountNumberGenerator()

        isRegistered = True

        
    def login(self):
        print(f"Hey! {name} Bienvenido al Banco de ColoTube")
        

    if isRegistered == False:
        registrarUsuario()
    
    else:
        login()
